from helium import *
import undetected_chromedriver as uc
import pandas as pd
import os
import tqdm
import re
driver = uc.Chrome()
url = 'https://yandex.ru'
options = uc.ChromeOptions()
options.add_argument('--proxy-server=195.29.77.19:8080')
set_driver(driver)
start_chrome(options=options)

go_to(url)

# Установить куки
path = "./ru/[RU]DESKTOP-0O7F8NF@user#473683fa1aa97786b73e38e08463c087/Browsers/"

cookies_chrome = pd.DataFrame(columns=['domain','httpOnly','path','sameSite','expiry','name','value'])
cookies_chrome_edge = pd.DataFrame(columns=['domain','httpOnly','path','sameSite','expiry','name','value'])
cookies_steam = pd.DataFrame(columns=['domain','httpOnly','path','sameSite','expiry','name','value'])
cookies_yandex = pd.DataFrame(columns=['domain','httpOnly','path','sameSite','expiry','name','value'])

cookies_other = pd.DataFrame(columns=['domain','httpOnly','path','sameSite','expiry','name','value'])

for file in tqdm.tqdm(os.listdir(path)):
    if file.endswith(".txt"):
        try:
            data = pd.read_csv(f"{path}/{file}",sep='\t',names=cookies_other.columns, header=None,encoding='utf-8')
            if "chrome" in file.lower():
                cookies_chrome = cookies_chrome.append(data)
            elif "chromium" in file.lower():
                cookies_chrome_edge = cookies_chrome_edge.append(data)
            elif "steam" in file.lower():
                cookies_steam = cookies_steam.append(data)
            elif "yandex" in file.lower():
                cookies_yandex = cookies_yandex.append(data)
            else:
                cookies_other = cookies_other.append(data)
        except Exception:
            pass

cookies_chrome = cookies_chrome.drop(columns=['sameSite','expiry'])
############ Установить куки
for cookie in cookies_chrome.to_dict(orient='records'):
    try:
        # проверка что куки от текущего юрла
        if re.search(cookie.get('domain'), url):
            driver.add_cookie(cookie_dict=cookie)

    except Exception as e:
        print(e)


# Перезагрузка
go_to(url)


kill_browser()
