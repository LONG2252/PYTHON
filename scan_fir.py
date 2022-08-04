#遍历一个文件夹，获取这个文件夹下所有的文件名，如果该文件夹下存在子文件夹，继续遍历

import os
from os import path as path

file_path=r"C:\Users\Alex\Desktop"

ss = os.listdir(file_path)

for row in ss:
    file_path=file_path + r'\\'+ row
    while(os.path.isdir(str(file_path))):
        new_file = file_path
        sr=os.listdir(new_file)
        for roe in sr:
            file_path=new_file + r'\\' + roe
    print(file_path)