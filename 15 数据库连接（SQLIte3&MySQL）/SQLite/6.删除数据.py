
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/20 08:48
# !/usr/bin/python3
# -*- coding:utf-8 -*-

#  导入模块
import sqlite3

# 链接数据库
con = sqlite3.connect(
    '/15 数据库连接（SQLIte3&MySQL）/SQLite/demo.db')
# 创建游标对象
cur = con.cursor()
# 指定删除的sql操作
sql_delete = 'delete from t_person where pno=?'

try:
    con.execute(sql_delete, (4,))
    con.commit()
    print("删除第四条数据成功")
except Exception as e:
    print(e)
    print('插入多条表内容失败')
    con.rollback()
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()