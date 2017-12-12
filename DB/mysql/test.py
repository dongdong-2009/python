# -*- coding:utf-8 -*-

import mysql.connector

if __name__ == "__main__":
    conn = mysql.connector.connect(user='root',password='111111',database='test')
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    conn.commit()
    cursor.close()