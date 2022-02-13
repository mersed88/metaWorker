from base64 import b64encode
import time
import requests
import undetected_chromedriver as uc
from helium import *

from pr import create_proxyauth_extension
import random

from helium import *
import undetected_chromedriver as uc


class Scenario:

    def __init__(self):
        ip = "77.37.172.20"
        port = 8195
        login = "ppbfic4uf"
        password = "gth8ji3ma7"

        self.driver = uc.Chrome()
        self.options = uc.ChromeOptions()

        proxyauth_plugin_path = create_proxyauth_extension(
            proxy_host=ip,
            proxy_port=port,
            proxy_username=login,
            proxy_password=password
        )

        self.options.add_argument("--start-maximized")
        self.options.add_extension(proxyauth_plugin_path)

        self.options.add_argument(f"--proxy-server={ip}:{port}")

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie_dict=cookie)

    def func_urls(self):
        urls = []
        urls.append('https://yandex.ru/news/?utm_source=main_stripe_big')
        urls.append('https://www.google.ru/webhp')
        urls.append('https://pikabu.ru/')
        urls.append('https://yandex.ru/')

        go_to(random.choice(urls))

    def func_wait(self):
        click(S('.TviglePlayer'))
        time.sleep(random.randint(6, 6 * 10))
        click(S('.TviglePlayer'))

    def func_exit(self):
        kill_browser()

    def func_ads(self):
        click(S('.turn-off-ads'))
        time.sleep(random.randint(6, 3 * 10))
        click(S('.close'))

    def start(self):
        set_driver(self.driver)
        start_chrome(options=self.options)
        url = 'http://v02.tvigle.ru/video/versus/season1/krutoi-protiv-tolpy-vd/?ref=1600'
        go_to(url)
        # helium.refresh()

        time.sleep(random.randint(37, 73))

        a = S('.TviglePlayer').exists()

        # b = S('.turn-off-ads').exists()

        # с = S('.close').exists()

        # print(a)
        # print(b)
        # print(с)

        if a:
            time.sleep(random.randint(5, 7))
            #     click(S('.turn-off-ads'))
            click(S('.TviglePlayer'))
            time.sleep(random.randint(59 * 10, 59 * 23))
            #     click(S('.TviglePlayer'))
            #     time.sleep(random.randint(6*1,6*2))

            getrandom = random.choice([self.func_urls, self.func_wait, self.func_exit, self.func_ads])
            getrandom()
            kill_browser()

        else:
            print('-kill_browser-')
            kill_browser()

if __name__ == '__main__':

    import pandas as pd
    pd.to_pickle(Scenario(), "scenario.pkl")
    # a = Scenario()
    # a.start()

