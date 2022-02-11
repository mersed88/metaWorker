import time

from helium import *
import undetected_chromedriver as uc

if __name__ =='__main__':

    driver = uc.Chrome()

    set_driver(driver)
    url = 'https://v02.tvigle.ru/video/versus/season1/krutoi-protiv-tolpy-vd/?ref=1600'
    go_to(url)

    a = S('.TviglePlayer').exists()
    print(a)
    if a:
        click(S('.TviglePlayer'))
    time.sleep(1000)
    kill_browser()