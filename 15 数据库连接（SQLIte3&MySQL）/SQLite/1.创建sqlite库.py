
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/20 07:24
# !/usr/bin/python3
# -*- coding:utf-8 -*-


import sqlite3
# db库所在路径
# /Users/ucloud/PycharmProjects/python_sql/SQLite/demo.db
con=sqlite3.connect('/15 数据库连接（SQLIte3&MySQL）/SQLite/demo.db')
# 获取cursor对象
cur = con.cursor()
# 执行sql创建表
sql = 'insert into t_person(pname,age) values(?,?)'
try:
    cur.execute(sql,("张三",24))
    print("插入表内容成功！")
    # 提交事务
    con.commit()
except Exception as e:
    print(e)
    print('创建表失败')
    con.rollback()
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()