import time
import random

from helium import *
import undetected_chromedriver as uc

if __name__ =='__main__':

    def func_urls():
        urls = []
        urls.append('https://yandex.ru/news/?utm_source=main_stripe_big')
        urls.append('https://www.google.ru/webhp')
        urls.append('https://pikabu.ru/')
        urls.append('https://yandex.ru/')

        go_to(random.choice(urls))


    def func_wait():
        click(S('.TviglePlayer'))
        time.sleep(random.randint(6, 6 * 10))
        click(S('.TviglePlayer'))


    def func_exit():
        kill_browser()


    def func_ads():
        click(S('.turn-off-ads'))
        time.sleep(random.randint(6, 3 * 10))
        click(S('.close'))


    driver = uc.Chrome()

    set_driver(driver)
    url = 'https://v02.tvigle.ru/video/versus/season1/krutoi-protiv-tolpy-vd/?ref=1600'
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
        time.sleep(random.randint(59*10, 59*23))
        #     click(S('.TviglePlayer'))
        #     time.sleep(random.randint(6*1,6*2))

        getrandom = random.choice([func_urls, func_wait, func_exit, func_ads])
        getrandom()
        kill_browser()

    else:
        print('-kill_browser-')
    #     kill_browser()



