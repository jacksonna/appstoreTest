from appium import webdriver

class Driver():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '华为p30'
    desired_caps['appPackage'] = 'com.qihoo.appstore'

    desired_caps['appActivity'] = '.home.MainActivity'
    desired_caps['skipServerInstallation'] = 'true' #已经安装过uiautomator2的两个服务，设定该配置，下次就不会再装了
    #desired_caps['automationName'] = 'Uiautomator1' # 不设置成Uiautomator1默认用的Uiautomator2，每次都会安装两个服务io.appium.uiautomator2.server
    # Uiautomator2解释 https://www.cnblogs.com/yyoba/p/9675071.html

    #desired_caps['autoLaunch'] = 'false' #不去自动启动设置的appActivity，会在当前界面执行后面的代码
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def close(self):
        self.close()
