#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""作业3
姓名: 邓钦元

要求:
为以下sql语句标注顺序 

答案:  每一句最后是顺序
SELECT DISTINCT player_id, player_name, count(*) as num  (5)
FROM player JOIN team ON player.team_id = team.team_id   (1)
WHERE height > 1.80   (2)
GROUP BY player.team_id   (3)
HAVING num > 2   (4)
ORDER BY num DESC   (6)
LIMIT 2  (7)
"""
