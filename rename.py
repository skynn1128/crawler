# -*- coding: utf-8 -*-
import os
#设定文件路径
path=r'C:\Users\jiangzhineng\Project\python_script\im'
i=1
#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
#设置新文件名
        new_name="im_car"+str(i)+".jpg"
#重命名
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
        i+=1
#结束
print ("End")

