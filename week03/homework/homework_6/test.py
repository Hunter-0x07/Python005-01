#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""作业6
姓名: 邓钦元

要求:
张三给李四通过网银转帐100极客币，现有数据库中三张表：

一张为用户表，包含用户ID和用户名字，另一张为用户资产表，包含
用户ID和用户总资产，第三张表为审计用表，记录了转帐时间，转帐id，
被转帐id，转帐金额

- 请合理设计三张表的字段类型和表结构；
- 请实现转帐100极客币的SQL（可以使用pymysql或sqlalchemy-orm实现)，
张三余额不足，转帐过程中数据库crash等情况需保证数据一致性

我的分析步骤如下:
（1）首先我确定每张表的名称以及字段所需要的名称及数据类型，
用户表 => users: 用户ID => user_id => Int  用户名字 => username String
用户资产表 => user_property: 用户ID => user_id => Int  用户总资产 => property => float
审计用表 => audit: 转帐时间 => transfer_time => date   
"""