#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""作业4
姓名: 邓钦元

要求:
以下两张基于id列，分别使用INNER JOIN,LEFT JOIN,RIGHT JOIN的结果是什么?
Table1
id name
1 table1_table2
2 table1

Table2
id name
1 table1_table2
3 table2

举例: INNER JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id

答案:
(1)对于INNER JOIN:
Table1和Table2的id相等的行

(2)对于LEFT JOIN:
Table1所有行,Table2中id和Table1相等的行

(3)对于RIGHT JOIN:
Table2所有行,Table1中id和Table2相等的行
"""