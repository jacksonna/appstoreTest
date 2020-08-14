import os
import time

import plotly.offline as py
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

#用list存储x和y轴的数据
datax = []
datay = []
for i in range(0,10):
    #获取内存值
    os.system('adb shell "dumpsys meminfo | grep com.qihoo.appstore" > D:/mem.txt')
    mems = open("D:/mem.txt",'r')
    mem = mems.readlines()
    qihoomem = mem[0].strip(' ').strip('/n').replace(',','')
    # w+ 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

    a = qihoomem.split(':')
    a = int(a[0].rstrip('K'))

    #print(a)
    b = format((a/1024),'.2f')
    print(b + 'MB')
    #用w+打开，会清除原有的数据
    mems = open("D:/activity.txt",'w+')
    datax.append(i)
    datay.append(b)
    time.sleep(5)
mems.close()

#给X和Y赋值
trace=go.Scatter(
    x = datax,
    y = datay
)
# 设置图表布局
layout = go.Layout(title="标题",xaxis={'title':'x轴'}, yaxis={'title':'y轴'})
#将layout设置到图表
fig = go.Figure(trace, layout=layout)
#绘图，并将图表保存到本地
py.plot(fig, filename = "D:/1.html")