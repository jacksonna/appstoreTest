import threading

class usb_install_thread(threading.Thread):
    def init(self):
        threading.Thread.__init__(self)
    def run():
        usb_install()
    def usb_install():
        while True:
            if flag == False:
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