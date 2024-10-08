# -*- coding: utf-8 -*-
# @Time : 2021/5/7
# @Author : J
# @File : zip.py
# @Software: PyCharm
# 导包
import zipfile
import os
 
 
month_rank_dir = "江志能-人脸"
zip_file_new = month_rank_dir+'.zip'
if os.path.exists(month_rank_dir):
    print('正在为您压缩...')
    # 压缩后的名字
    zip = zipfile.ZipFile(zip_file_new, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(month_rank_dir):
        # 去掉目标跟路径，只对目标文件夹下面的文件及文件夹进行压缩
        fpath = dir_path.replace(month_rank_dir, '')
        for filename in file_names:
            zip.write(os.path.join(dir_path, filename), os.path.join(fpath, filename))
    zip.close()
    print('该目录压缩成功！')
else:
    print('您要压缩的目录不存在...')





