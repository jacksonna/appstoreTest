#获取启动速度
import os
import time
import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import appiumtest

#os.system('adb uninstall com.qihoo.appstore')
#print(os.system('adb install C:/Users/dongna/Desktop/360box_update.apk'))

#启动app并获取启动时间
def start():
    # os.popen() 方法用于从一个命令打开一个管道。可以输出adb命令的返回值
    content = os.popen('adb shell am start -W -n com.qihoo.appstore/.home.MainActivity')
    for line in content.readlines():
        if "WaitTime" in line:
            sTime = line.split(':')[1]
    #print(sTime)
    return sTime

#强制停止app
def clodStop():
    os.system('adb shell am force-stop com.qihoo.appstore')

#home退出app
def homeStop():
    os.system('adb shell input keyevent 3')

#back退出app
def backStop():
    os.system('adb shell input keyevent 4')
    os.system('adb shell input keyevent 4')

#首次启动时间
def firstStartTime():
    os.system('adb uninstall com.qihoo.appstore')
    os.system('adb install C:/Users/dongna/Desktop/360box_update.apk')
    print("首次启动时间：" + start())

#平均启动时间
def averageStartTime(num:int):
    count = num
    time = 0
    while num > 0:
        clodStop()
        time += int(start())
        num -= 1
    avST = format(time/count,'.2f')
    print("强制停止后启动时间：" + avST)

#首页加载速度
def homepageShowTime():
    clodStop()
    start()
    #检测到当前是首页activity开始计时
    while appiumtest.focActivity("com.qihoo.appstore.home.MainActivity"):
        print(1)
    #记录当前时间戳
    startTime = time.time()
    print(startTime)
    #检测到出现“今日热点”，表示首页加载出来
    driver = appiumtest.Driver().div()
    try:
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'今日热点')]")
    except:
        print("没找到元素") 
    else:
        endTime = time.time()
        print(endTime)
    showTime = endTime-startTime
    print(format(showTime,'.2f'))

#用list存储x和y轴的数据
clodx = []
clody = []
backx = []
backy = []
#启动时间
def oneStartTime(num:int):
    for i in range(0,num):
        backx.append(i)
        backStop()
        time.sleep(2)
        backy.append(start())
        time.sleep(2)
        clodx.append(i)
        clodStop()
        time.sleep(2)
        clody.append(start())
        time.sleep(2)
    pic()

#绘制折线图
def pic():
    #给X和Y赋值
    trace1 =go.Scatter(
        x = clodx,
        y = clody,
        name = "强制停止后启动时间"
    )
    trace2 =go.Scatter(
        x = backx,
        y = backy,
        name = "back退出后启动时间"
    )
    trace = [trace1,trace2]
    # 设置图表布局
    layout = go.Layout(title="安装后启动时间",xaxis={'title':'启动次数'}, yaxis={'title':'时间'})
    #将layout设置到图表
    fig = go.Figure(trace,layout=layout)
    #绘图，并将图表保存到本地
    py.plot(fig, filename = "F:/python/app/安装后启动时间.html")

#oneStartTime(3)
homepageShowTime()