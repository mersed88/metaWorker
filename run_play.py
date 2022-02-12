import time
import random

from helium import *
import undetected_chromedriver as uc

if __name__ =='__main__':

    def func1():
        url = 'https://v02.tvigle.ru/video/versus/season1/krutoi-protiv-tolpy-vd/?ref=1600'
        go_to(url)


    def func2():
        print("пукпук2")


    def func3():
        print("пукпук3")

    driver = uc.Chrome()

    set_driver(driver)
    url = 'https://v02.tvigle.ru/video/versus/season1/krutoi-protiv-tolpy-vd/?ref=1600'
    go_to(url)

    time.sleep(random.randint(30,50))

    a = S('.TviglePlayer').exists()
    print(a)
    if a:
        click(S('.TviglePlayer'))

    time.sleep(random.randint(60*60*10,60*60*20))

    getrandom = random.choice([func1, func2, func3])
    getrandom()

    kill_browser()



