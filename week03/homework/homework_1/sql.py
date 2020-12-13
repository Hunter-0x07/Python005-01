#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""作业1
姓名: 邓钦元

要求如下:
（1）将修改字符集的配置项，验证字符集的SQL语句作为作业内容提交
（2）将增加远程用户的SQL语句作为作业内容提交
"""

if __name__ == "__main__":
    modify_charset = """
    [client]
    default_character_set = utf8mb4

    [mysql]
    default_character_set = utf8mb4

    character_set_server = utf8mb4  # MySQL字符集设置
    init_connect = 'SET NAMES utf8mb4'  # 服务器为每个连接的客户端执行的字符串
    """
    verify_charset = "SHOW VARIABLES LIKE '%character%'"
    add_remote_user = "GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass'"