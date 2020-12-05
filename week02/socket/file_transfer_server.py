#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import tqdm
import os
import logging

# Hostname or IP address of the device
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


def echo_server():
    """ Receive file as server """
    # Modify basic config of logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S")

    # Create the server socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to our local address
    s.bind((SERVER_HOST, SERVER_PORT))

    # Enabling our server to accept connections
    s.listen(5)
    logging.info(f"[*] Listenning as {SERVER_HOST} {SERVER_PORT}")

    # Accept connection if there is any
    client_socket, address = s.accept()
    logging.info(f"[+] {address} is connected.")
    received = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    filename, filesize = received.split(SEPARATOR)

    # Remove absolute path if there is
    filename = "Accept_" + os.path.basename(filename)

    # Convert filesize to integer
    filesize = int(filesize)

    # Start receiving the file from the socket
    # and write it to the file stream
    progress = tqdm.tqdm(range(filesize), f'Receiving {filename}',
                            unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for _ in progress:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break

            # Update the progress bar
            progress.update(len(bytes_read))

    # Close the client socket
    client_socket.close()

    # Close the server socket
    s.close()


def main():
    """ Entrance of the program """
    echo_server()


if __name__ == "__main__":
    main()
