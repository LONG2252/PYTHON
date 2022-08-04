# -*- coding:utf-8 -*-
import os
def Ping(ip_list):
    status=[]
    for ip in ip_list:
        result = os.system(u"ping  %s" % (ip))
        s={'ip':ip,'result':result}
        status.append(s)
    return status;
def CreatIP():
    ip_list=[]
    #value_1=1
    for value_1 in range(1,2):
        for value_2 in range(1,7):
            ip = "192.168." + str(value_1) + "." + str(value_2)
            ip_list.append(ip)
    return ip_list;

IP_LIST=CreatIP()
status=Ping(IP_LIST)
path=r"C:\Users\Alex\Documents\Code\ip_information.txt"
f=open(path ,'a')

for row in status:
    #print(type(row['ip']))
    #print(type(row['result']))
    massage="ip:"+ row['ip']+"   "+"status:"+str(row['result'])
    f.write(massage)
    f.write("\n")
f.close()

