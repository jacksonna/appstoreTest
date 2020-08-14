from appium import webdriver
import threading
import os
import time
class usb_install_thread(threading.Thread):
    def init(self):
        threading.Thread.__init__(self)
    def run(self):
        self.usb_install()
    def usb_install(self):
        while True:
            if flag == False:
                print("结束")
                break
            try:
                em = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'继续安装')]")
                if em:
                    em.click()
            except:
                pass
            try:
                em =driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]")
                if em:
                    em.click()
            except:
                pass
            try:
                em = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'确认')]")
                if em:
                    em.click()
            except:
                pass

#配置appium setting为被测App
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = '华为p30'
desired_caps['appPackage']='io.appium.settings'
desired_caps['appActivity']='io.appium.settings.Settings'
desired_caps['autoGrantPermissions']= True
desired_caps['skipServerInstallation'] = 'true' #已经安装过uiautomator2的两个服务，设定该配置，下次就不会再装了
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#flag先置为True，检测安装弹窗
flag = True
#创建线程
thread = usb_install_thread()
#启动线程
thread.start()
#安装成功将flag置为0，结束线程
flag = os.system('adb install C:/Users/dongna/Desktop/360box_update.apk')
#等两秒，判断线程是否还活着。false表示结束
time.sleep(2)
print(thread.is_alive())