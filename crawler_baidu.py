import os
import requests
import re
import time

def get_parse_page(pn, name):

# 获取图片url连接
    for i in range(int(pn)):
        # 1.获取网页
        print('正在获取第{}页'.format(i+1))

        # 百度图片首页的url
        # name是你要搜索的关键词
        # pn是你想下载的页数

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' %(name,i*20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}

        # 发送请求，获取相应
        response = requests.get(url, headers=headers)
        html = response.content.decode()
        # print(html)
        time.sleep(2)
        # 2.正则表达式解析网页
        # "objURL":"http://n.sinaimg.cn/sports/transform/20170406/dHEk-fycxmks5842687.jpg"
        results = re.findall('"objURL":"(.*?)",', html) # 返回一个列表

        # 根据获取到的图片链接，把图片保存到本地
        save_to_txt(results, name, i)



def save_to_txt(results,name,i):
# 保存图片到本地
    j = 0
    # 在当目录下创建文件夹
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    # 下载图片
    for result in results:
        print('正在保存第{}个'.format(j))
        try:
            pic = requests.get(result, timeout=10)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        # 把图片保存到文件夹
        file_full_name = './' + name + '/' + str(name) + '-' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f :
            f.write(pic.content)

        j +=1



# 主函数
if __name__ == '__main__':

    # name = input('请输入你要下载的关键词：')
    # pn = input('你想下载前几页（1页有60张）:')
    # classlist = ["键盘", "keyboard","轿车内部","incar","教室", "classroom" ,"酒吧" ,"bar","客厅" ,"livingroom", "空调", "airconditioner","孔雀" ,"peacock"]
    # keyboardlist = ["电脑键盘","黑色键盘","彩色键盘","机械键盘","白色键盘","有线键盘","无线键盘"]
    # classroomlist = ["课堂","大学课堂","高中课堂","初中课堂","大学教室","高中教室","初中教室","小学教室","大教室","小教室","智慧教室","乡村教室","美国教室","学校教室"]
    # barlist = ["上海酒吧","深圳酒吧","杭州酒吧","北京酒吧"]
    # livingroomlist = ["中式客厅","欧式客厅","美式客厅","简约客厅"]
    # carlist = ["车内","豪车内饰","车内饰","车中控台","豪车中控台","车方向盘","豪车方向盘","车座椅","豪车座椅"]
    # airconditionerlist = ["挂壁式空调","立柜式空调","窗式空调","吊顶式空调","中央空调","格力空调","海尔空调","美的空调","居家空调"]
    # peacocklist = ["蓝孔雀" ,"绿孔雀" ,"刚果孔雀","野生孔雀","养殖孔雀"]
    # otherlist = ["airconditioner","空调图片","新空调","车座椅","豪车座椅","白色空调"]
    # mountainlist = ["山峰","山","峰","群山","山顶","高山","雪山","山脉"]
    # mingshanglist = ["泰山","黄山","峨眉山","庐山","珠穆朗玛峰","长白山","华山","武夷山","玉山","五台山","雁荡山","嵩山","梵净山","昆仑山","天柱山","冈仁波齐","卡瓦格博","喜马拉雅","梅里雪山","南迦巴瓦峰","喜马拉雅山","富士山","安第斯山","阿尔卑斯山","落基山","乞力马扎罗山"]
    # worldmountainlist = ["喜马拉雅山脉","锡安山","麦金利山","南迦帕尔巴特","干城章嘉峰","博格达峰","贡嘎峰"]
    # newmountainlist = ["乔戈里峰","洛子峰","马卡鲁峰","卓奥友峰","道拉吉里峰","马纳斯卢峰","安那布尔纳峰"]
    # face = ["老人照片","农村老年人照片","老人图片","暴雨行人","大雨行人","雨中人","暴雨中人","北京雾霾人","西安雾霾人","上海雾霾人","模糊头像","模糊半身像","女生模糊头像","模糊头像男"]
    # rainlist = ["雨戏","淋雨戏"]
    # horselist = ["马"]
    # horselist = ["马","人","人和马","马和猫","人和猫","人和狗","马和狗"]
    horselist = ["智己汽车实拍"]
    pn = 10
    for name in horselist:
        get_parse_page(pn, name)
