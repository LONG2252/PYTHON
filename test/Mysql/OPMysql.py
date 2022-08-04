#!/usr/bin/python3
import pymysql


class OPMysql():
    def Con(self):
        try:
            self.connect=pymysql.connect(
                host='192.168.1.2',
                port=3306,
                db='',
                user='root',
                passwd='*******',
                charset='utf8',
                database='User'
            )
            return 1
        except Exception as e:
            return (e)
    def CreTab(self):
        if self.Con():
            self.cursor=self.connect.cursor()
        SQL="""
        SHOW TABLES;
        """
        try:
            self.cursor.execute(SQL)
            return self.cursor.fetchall()
        except Exception as e:
            return e
        self.connect.close()
    def add(self,):
        SQL="""
        
        
        """

CreT=OPMysql()
print(CreT.CreTab())