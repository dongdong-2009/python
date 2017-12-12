# -*- coding:utf-8 -*-

import sqlite3

if __name__ == "__main__":
    op = "get"
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    #cursor.execute('create table user (id varchar(20) PRIMARY KEY ,name VARCHAR(20))')

    if op == "insert":
        cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
        print(cursor.rowcount)
    elif op == "get":
        cursor.execute('select * from user where id=?', ('1',))
        values = cursor.fetchall()
        print(values)
    cursor.close()
    conn.commit()
    conn.close()