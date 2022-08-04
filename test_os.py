#将所有可读文件的内容读出来

import os

file_path=r"C:\Users\Alex\Desktop"

ss=os.listdir(file_path) #遍历path路径下所有文件的文件名
add_file=r"C:\Users\Alex\Desktop\111.txt"
for row in ss:
    file_name = file_path + r"\\" + row   #创建path路径下文件的绝对路径文件名
    file_inf=os.path.splitext(file_name)   #将创建file_name文件格式为（文件名，文件拓展名）的元组
    if(file_inf[1] in ('.txt','.py','.sh')): #如果file_name文件的拓展名是可识别的(格式为.txt .py .sh）

    #print(os.path.isfile(file_name))
    # if os.path.isfile(file_name):
        file_new = open(file_name, 'r', encoding='utf-8')    #打开该文件
        file_old = open(add_file,'a',encoding='utf-8')

        try:
            file_old.write(file_new.read())  # 读取文件内容
            print("写入成功！")
        except Exception as e:
            print(e)
        file_old.close()
        file_new.close()     #关闭文件！
    # else:
    #     print( "%s is not a file " %row)
