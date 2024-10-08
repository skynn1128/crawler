import os
import cv2
import numpy as np


img_path = r"C:\Users\jiangzhineng\Project\python_script\智己汽车实拍"
for img in os.listdir(img_path):
    img_name = os.path.join(img_path,img)
#     print(img_name)
    try:
    # cv2.imdecode(np.fromfile("C:\Projects\pachon\有线键盘\有线键盘-9-9.jpg",dtype=np.uint8),-1)
        img1 = cv2.imdecode(np.fromfile(img_name,dtype=np.uint8),-1)
        # print(img1.shape)
        h,w,c = img1.shape
        assert h > 10 or w > 10
    except:
        os.remove(img_name)