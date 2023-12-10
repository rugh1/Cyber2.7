# Cyber2.7 Project - Server and Client

## Server

### Author: Rugh1
### Date: 10.12.2023
### Description: Server for Cyber2.7 Work

### Overview

This project consists of a server and a client designed for Cyber2.7 work. The server handles incoming connections and communication with clients, executing various commands sent by clients. The client connects to the server, sends commands, and receives responses.

### Server Features

- **Logging**: The server logs events such as client connections, received requests, and disconnections. Log files are stored in the 'log' directory.

- **Communication Protocol**: The server uses a custom communication protocol implemented in the 'protocol' module to send and receive data between the server and clients.

- **Command Handling**: The server processes commands received from clients using the 'functions' module. Commands include DIR, DELETE, COPY, EXECUTE, and more.

### Server Configuration

- **IP and Port**: The server is configured to listen on IP address '127.0.0.1' and port '25565'.

- **Maximum Packet Size**: The maximum packet size for communication is set to 1024 bytes.

- **Queue Length**: The server accepts only one connection at a time with a queue length of 1.

### Commands

1. **DIR Command**
    - **Description**: List files in a directory.
    - **Usage**: `DIR path`
    - **Example**: `DIR C:\Users`

2. **DELETE Command**
    - **Description**: Delete a file.
    - **Usage**: `DELETE path`
    - **Example**: `DELETE C:\Files\example.txt`

3. **COPY Command**
    - **Description**: Copy a file.
    - **Usage**: `COPY source_path destination_path`
    - **Example**: `COPY C:\Files\file.txt D:\Backup`

4. **EXECUTE Command**
    - **Description**: Execute a command.
    - **Usage**: `EXECUTE command`
    - **Example**: `EXECUTE notepad.exe`

5. **TAKE_SCREENSHOT Command**
    - **Description**: Take a screenshot and save it as 'screen.jpg'.
    - **Usage**: `TAKE_SCREENSHOT`
    - **Example**: `TAKE_SCREENSHOT`

### How to Run

1. Ensure the 'protocol' module is available.
2. Run the server script.
3. The server will wait for incoming connections.
4. Clients can connect and send commands to the server.

```bash
python server.py
```

## Sequence Diagram

![Sequence Diagram](https://github.com/rugh1/Cyber2.7/raw/master/diagram.png)

...
