#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Title: transfer file by socket

#学号: G20200389060133
#姓名: 邓钦元
#作业&总结链接: https://github.com/Hunter-0x07/Python005-01/tree/main/week02
"""

import socket
import os
import tqdm
import logging

SEPARATOR = "<SEPARATOR>"

# send 4096 bytes each time step
BUFFER_SIZE = 4096

# The ip address or hostname of the server, the receiver
HOST = "localhost"
PORT = 5001

# The name of the file we want to send, make sure it exists
FILENAME = "index.html"

# Get the size of file
FILESIZE = os.path.getsize(FILENAME)


def echo_client():
    """ Transfer File's Client """
    # Modify logging basic config
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    # Create the client socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the server
    logging.info(f"[+] Connecting to {HOST} {PORT}.")
    try:
        s.connect((HOST, PORT))
        logging.info("[+] Connected.")
    except Exception as e:
        logging.error(f"Failed to connect: {e}")

    # Send the filename and filesize
    s.send(f"{FILENAME}{SEPARATOR}{FILESIZE}".encode())

    # Start sending the file
    progress = tqdm.tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B",
                         unit_scale=True, unit_divisor=1024)

    with open(FILENAME, 'rb') as f:
        for _ in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # Close the socket
    s.close()


def main():
    """ Entrance of program """
    echo_client()


if __name__ == "__main__":
    main()
