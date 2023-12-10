"""
Author: Rugh1
Date: 10.12.2023
Description: client for cyber2.7 work
"""
import base64
from io import BytesIO
import socket
import re
import logging
import os
import traceback
from protocol import *
from PIL import Image

IP = '127.0.0.1'
PORT = 25565
INPUT_MESSAGE = "enter from the following commands: DIR path , DELETE path ,  COPY path_to_copy_from path_to_copy_to , EXECUTE path , TAKE_SCREENSHOT , SEND_PHOTO , EXIT"
COMMAND_PATTERN = re.compile(r'^(DIR|DELETE|COPY|EXECUTE|TAKE_SCREENSHOT|SEND_PHOTO|EXIT)(?:\s[\w\s.:/\\]+)?$')

# Configuration for logging
LOG_FORMAT = '%(levelname)s | %(asctime)s | %(processName)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/client.log'

def main():
    """
    Connect to the server and send commands.

    :return: None
    :rtype: None
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((IP, PORT))
        no_exit = True
        while no_exit:
            request = input(INPUT_MESSAGE + ': ')
            logging.debug(f"request: {request}")
            print(request)
            if COMMAND_PATTERN.match(request):
                send(client_socket, request)
                response = ' '.join(recv(client_socket))
                if 'SEND_PHOTO' in request:
                    decoded_string = base64.b64decode(response)
                    try:
                        image = Image.open(BytesIO(decoded_string))
                        image.show()
                    except Exception as err:
                        print("check if screenshot exists" + str(err))
                    
                else:
                    print(response)
                    no_exit = "EXIT" not in request
                    logging.debug(f"Received response: {response}")
            else:
                print(f"Please enter one of the following commands: {INPUT_MESSAGE} or provide a correct path")

    except Exception as err:
        # Log exceptions
        print(traceback.format_exc())
        logging.error(err)
    finally:
        # Close the client socket
        try:
            send(client_socket, "client crashed")
        except Exception:
            pass
        finally:
            client_socket.close()
            logging.info("Disconnected from the server")


if __name__ == '__main__':
    """
    Configure logging and run the client.

    :return: None
    :rtype: None
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)
    assert COMMAND_PATTERN.match(r"DIR C:\Users")
    assert COMMAND_PATTERN.match(r"DELETE C:\Users")
    assert COMMAND_PATTERN.match(r"COPY C:\randompath\file1 C:\randompath\file2")
    assert COMMAND_PATTERN.match(r"EXECUTE C:\Windows\System32\notepad.exe")
    assert COMMAND_PATTERN.match(r"TAKE_SCREENSHOT")
    assert COMMAND_PATTERN.match(r"SEND_PHOTO") 
    main()