# -*- coding: UTF-8 -*-
import socket

s=socket.socket()
host=socket.gethostname()
port=12123
s.bind((host,port))

s.listen(5)
while True:
    c,addr=s.accept()
    print("连接地址：",addr)
    msg="欢迎连接！"
    c.send(msg.encode("utf-8"))