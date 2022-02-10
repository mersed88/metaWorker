import undetected_chromedriver as uc
from helium import *


class Scenario:
    def __init__(self):
        self.driver = uc.Chrome()
        self.options = uc.ChromeOptions()

    def add_proxy(self, ip):
        self.options.add_argument(f'--proxy-server={ip}')

    def run(self, url):
        set_driver(self.driver)
        start_chrome(options=self.options)
        go_to(url)


    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie_dict=cookie)

    def exit(self):
        kill_browser()



if __name__ == '__main__':
    Scenario().run("yandex.ru")
