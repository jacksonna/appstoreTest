#coding=utf-8
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import os
class Driver():
    def div(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '华为p30'
        desired_caps['appPackage'] = 'com.qihoo.appstore'

        desired_caps['appActivity'] = '.home.MainActivity'
        desired_caps['skipServerInstallation'] = 'true' #已经安装过uiautomator2的两个服务，设定该配置，下次就不会再装了
        #desired_caps['automationName'] = 'Uiautomator1' # 不设置成Uiautomator1默认用的Uiautomator2，每次都会安装两个服务io.appium.uiautomator2.server
        # Uiautomator2解释 https://www.cnblogs.com/yyoba/p/9675071.html

        desired_caps['autoLaunch'] = 'false' #不去自动启动设置的appActivity，会在当前界面执行后面的代码
        desired_caps['noReset'] = True
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10) #隐式等待，对所有的查找元素都会执行改方法，等待10s，如果在10s内找到了就停止等待；没找到10s后结束等待
        return driver
    def __del__(self):
        driver.close()

#la = driver.find_elements_by_xpath("//*[contains(@text, '打开')]")
driver = Driver().div()
#print("生成driver")
def jietu():
    for i in range(161,207):
        #使用xpath找到“今日热点”的打开按钮
        la = driver.find_elements_by_xpath("//android.view.View/android.view.View/android.widget.ListView/android.view.View[contains(@index,{})]/android.view.View[3]".format(i))

       #如果没找到“打开”按钮就上滑再找
        j = 0
        while len(la) == 0 and j < 2:
        #上滑
            driver.swipe(580,2100,580,1000)
            la = driver.find_elements_by_xpath("//android.view.View/android.view.View/android.widget.ListView/android.view.View[contains(@index,{})]/android.view.View[3]".format(i))
            j += 1
        #上滑两次找不到就退出
        if j >= 2:
            print("找不到元素" + str(i))
            return

        #使用xpath找到“今日热点”的应用名称
        nameL = driver.find_elements_by_xpath("//android.view.View/android.view.View/android.widget.ListView/android.view.View[contains(@index,{})]/android.view.View[1]".format(i))
        if len(nameL) > 0:
            name = nameL[0].text
        
        #点击“打开”按钮
        la[0].click()

        #等待5s跳转到微信打开小程序
        time.sleep(5)

        #截图并保存到文件夹，文件名使用应用名加位置
        driver.get_screenshot_as_file("D:/picture/" + str(i) + name + ".png")

        #如果弹窗按钮有“确定”，就先点击确定。点击back键返回小程序页面
        try:
            button = driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[contains(@text,'确定')]")
        except NoSuchElementException:
            driver.press_keycode(4)
        else:
            button.click()
            print(name)
        while focActivity("con.qihoo.appstore"):
            driver.press_keycode(4)

def focActivity(focActivity):
    #print("开始查找")
    os.system('adb shell dumpsys window | findstr mCurrentFocus > D:/activity.txt')
    text = open("D:/activity.txt",'r')
    activity = text.readlines()
    com = activity[0].strip('\n')
    if focActivity in com:
        return False
    else:
        return True
    #w+ 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    text = open("D:/activity.txt",'w+')
    text.close()

#jietu()
#driver.close()