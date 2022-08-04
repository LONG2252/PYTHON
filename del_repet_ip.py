import re


old_ip_list_path=r'/data/defence/loging_log/all_login_success_ip.log'
new_ip_list_path=r'/data/defence/loging_log/login_success_ip_list.log'

old_ip_list_orgin=open(old_ip_list_path,mode='r')
old_ip_list_whole=old_ip_list_orgin.read()
old_ip_list=re.split('\n',old_ip_list_whole)

new_ip_list_orgin=open(new_ip_list_path,mode='w+')
moment_list=[]
for row in old_ip_list:
    if(row not in moment_list):
        moment_list.append(row)
        new_ip_list_orgin.write(row+"\n")
old_ip_list_orgin.close()
new_ip_list_orgin.close()