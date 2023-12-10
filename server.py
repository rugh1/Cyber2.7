import socket
import logging
import os
from protocol import *
import functions
import traceback

# Configuration for logging
LOG_FORMAT = '%(levelname)s | %(asctime)s | %(processName)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE =  LOG_DIR + '/server.log'

# Server configuration
IP = '127.0.0.1'
PORT = 25565
MAX_PACKET = 1024
QUEUE_LEN = 1
DISCONNECT_MESSAGE = "bye now"


def handle_client(client_socket, client_address):
    """
    Handle communication with a connected client.

    :param client_socket: Socket object for communication with the client.
    :type client_socket: socket.socket

    :param client_address: Tuple representing the client's address (IP, port).
    :type client_address: tuple

    :return: None
    :rtype: None
    """
    try:
        # Log when a client is connected
        logging.info(f"Connected with: {client_address}")
        print(f"Connected with: {client_address}")
        while True:
            # Receive the request from the client
            request = recv(client_socket)
            # Log the received request
            logging.debug(f"Received request: {request}")

            # Get the appropriate command handler and execute it
            command_handler = getattr(functions, f'{request[0].lower()}_cmd')
            response = command_handler(request)
            # Log the response before sending it back to the client
            logging.debug(f"Sending response: {response}")
            
            # Send the response back to the client
            send(client_socket, response)

            # If the client sent an EXIT command, log and break out of the loop
            if request[0] == 'EXIT':
                logging.info("Disconnecting client...")
                break

    except socket.error:
        # Log socket errors
        print(traceback.format_exc())
        logging.error(traceback.format_exc())
    except Exception:
        # Log other exceptions
        print(traceback.format_exc())
        logging.error(traceback.format_exc())
    finally:
        # Close the client socket and log the disconnection
        client_socket.close()
        logging.info("Disconnected client")


def run_server():
    """
    Run the server to accept incoming connections and handle clients.

    :return: None
    :rtype: None
    """
    print("nana")
    try:
        # Set up the server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((IP, PORT))
        server_socket.listen(QUEUE_LEN)
        print("nana")
        while True:
            # Wait for incoming connections
            logging.info("Waiting for connections...")
            print("Waiting for connections...")
            client_connection, client_address = server_socket.accept()
            # Handle the connected client
            handle_client(client_connection, client_address)

    except socket.error as err:
        # Log socket errors
        logging.error(err)
    finally:
        # Close the server socket when done
        server_socket.close()


if __name__ == '__main__':
    """
    Configure logging and run the server.

    :return: None
    :rtype: None
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)
    run_server()