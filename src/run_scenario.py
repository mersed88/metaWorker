from base64 import b64encode
import time
import requests
import undetected_chromedriver as uc
from helium import *

from pr import create_proxyauth_extension


class Scenario:
    def __init__(self):
        ip = "77.37.172.20"
        port = 8195
        login = "ppbfic4uf"
        password = "gth8ji3ma7"


        self.driver = uc.Chrome()
        self.options = uc.ChromeOptions()

    def add_options(self, option):
        self.options.add_argument(f'{option}')

    def run(self, url):
        set_driver(self.driver)
        start_chrome(options=self.options)
        go_to(url)

    def go_to(self,url):
        go_to(url)


    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie_dict=cookie)

    def exit(self):
        kill_browser()



if __name__ == '__main__':
    import time
    ip = "77.37.172.20"
    port = 8195
    login = "ppbfic4uf"
    password = "gth8ji3ma7"

    driver = uc.Chrome()
    options = uc.ChromeOptions()
    set_driver(driver)

    proxyauth_plugin_path = create_proxyauth_extension(
        proxy_host=ip,
        proxy_port=port,
        proxy_username=login,
        proxy_password=password
    )

    options.add_argument("--start-maximized")
    options.add_extension(proxyauth_plugin_path)

    options.add_argument(f"--proxy-server={ip}:{port}")
    start_chrome(options=options)
    go_to("https://api.ipify.org")
    time.sleep(3)
