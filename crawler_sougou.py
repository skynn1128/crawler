import requests
from urllib.parse import quote
import os

# 搜索的内容
key = quote('男生侧颜')

# 第几页, 每一页有48张图片。每一页的开始是48的倍数
page=200
k=0
for i in range(int(page)):
    start = i * 48
# 拼接url链接
# .format的括号（）里面的会代替花括号{}，且按顺序一对一，例如第一个{}用start代替，第二个{}用key代替
    url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start={}&xml_len=48&query={}'.format(start,key)

# 发送请求，对url对应的服务器发送
    response = requests.get(url)

# response把它转化为json的数据格式，才能用类似于字典的数据，来获取对应的值
    json_data = response.json()

    all_data = json_data['data']['items']

    # 图片的url，下载图片的url
    pic_urls=[]
    # 图片的title，保存图片的名字
    pic_titles=[]
    for data in all_data:
        url = data['thumbUrl']
        # 把url添加到pic_urls
        pic_urls.append(url)

        # 把title添加到pic_titles
        title = data['title']
        pic_titles.append(title)



    # 保存
    for number in range(len(pic_titles)):
        data=requests.get(pic_urls[number]).content

        # 写入文件，以jpg
        with open('./男生侧颜/'+str(k)+'.jpg','wb')as file:
            file.write(data)
        k=k+1
        print(k,'-----------------',pic_titles[number],'下载好了------------------')