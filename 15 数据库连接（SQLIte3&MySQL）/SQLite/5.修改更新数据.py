
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/20 07:52
# !/usr/bin/python3
# -*- coding:utf-8 -*-


import sqlite3
# db库所在路径
# /Users/ucloud/PycharmProjects/python_sql/SQLite/demo.db
con = sqlite3.connect(
    '/15 数据库连接（SQLIte3&MySQL）/SQLite/demo.db')
# 获取cursor对象
cur = con.cursor()
sql = 'select * from t_person'
try:
    #执行sql创建表
    update_sql = 'update t_person set pname=? where pno=?'
    cur.execute(update_sql, ('方胜山', 4))
    con.commit()
    print("修改成功")
except Exception as e:
    print(e)
    print('插入多条表内容失败')
    con.rollback()
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()
