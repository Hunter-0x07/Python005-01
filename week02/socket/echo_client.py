#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
import sys


SERVER_HOST = "localhost"
SERVER_PORT = 53454


def echo_client():
    """ Echo Client """
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接目标服务器
    try:
        logging.info("尝试连接目标服务器")
        s.connect((SERVER_HOST, SERVER_PORT))
        logging.info("连接成功!")
    except Exception as e:
        logging.info(f"连接失败: {e}")

    # 等待用户输入文本
    while True:
        send_data = input(f"请输入要发送的信息=>")

        if send_data == "exit":
            sys.exit()

        if send_data:
            # 向服务器发送用户输入文本
            s.sendall(send_data.encode())
            logging.info("信息已发送!")
            break

    # 准备接收数据
    logging.info("准备接收数据...")

    # 创建列表接收返回的信息
    buffer = []

    # 接收返回信息
    while True:
        recv_data = s.recv(2048)
        if recv_data:
            logging.info(f"接收到数据...")
            buffer.append(recv_data)
        else:
            break

    # 处理并展示返回的数据
    r_data = b''.join(buffer)
    logging.info(f"接收信息为: {r_data}")

    # 关闭连接
    s.close()


if __name__ == "__main__":
    echo_client()
