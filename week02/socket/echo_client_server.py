#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging

HOST = "localhost"
PORT = 53452


def echo_server():
    """ Echo Server"""
    # 配置日志选项
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S"
    )

    # 创建Socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定主机及端口号
    s.bind((HOST, PORT))

    # 监听端口，默认允许5个连接
    s.listen(5)

    # 等待接收连接请求
    while True:
        logging.info("等待连接...")
        # 等待连接，程序进入阻塞状态
        conn, addr = s.accept()
        logging.info(f"连接成功，客户端IP地址为{addr}")

        # 尝试读取数据
        while True:
            data = conn.recv(2048)
            if not data:
                logging.info("没有数据，断开连接")
                conn.close()
                break
            else:
                try:
                    conn.sendall("你发送的信息是:".encode() + data)
                    logging.info("已向客户端发送数据，关闭连接")
                    conn.close()
                    break
                except Exception as e:
                    logging.error(f"发送失败: {e}")
                    conn.close()
                    break

    # 关闭连接
    s.close()


if __name__ == "__main__":
    echo_server()
