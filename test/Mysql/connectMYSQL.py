#!/usr/bin/python3
import pymysql

db=pymysql.connect(
    host='192.168.1.2',
    port=3306,
    db='',
    user='root',
    passwd='*******',
    charset='utf8'
)
#def
cursor=db.cursor()
sql="SHOW DATABASES;"
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        print(row)
except Exception as e:
    print(e)
db.close()