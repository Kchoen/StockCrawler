from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import TRACK_UpdateData
stockNums = input("輸入要下載的股號(可批量下載)：")
print('下載股號為：',stockNums.split(' '))
for stockNum in stockNums.split(' '):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': "C:\\Users\\User\\Desktop\\data\\tmp"}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome = webdriver.Chrome('./chromedriver',options = options)
    chrome.get("https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html")

    Typein = chrome.find_element_by_name("stockNo")
    s1 = Select(chrome.find_element_by_name('yy'))
    s2 = Select(chrome.find_element_by_name('mm'))
    Typein.send_keys(stockNum)    

    months = 0
    for select1 in s1.options:
        select1.click()
        for select2 in s2.options:
            select2.click()
            Typein.submit()
            time.sleep(1)
            try:
                link = chrome.find_element_by_link_text('CSV 下載')
                link.click()
            except:
                break


            time.sleep(4)
            months+=1


    s1.options[0].click()
    s2.options[len(s2.options)-1].click()
    Typein.submit()
    time.sleep(1)
    try:
        link = chrome.find_element_by_link_text('CSV 下載')
        link.click()
    except:
        print("股號:{} 無法下載.".format(stockNum))
        break    
    time.sleep(3)
    s2.options[len(s2.options)-2].click()
    Typein.submit()
    time.sleep(1)
    try:
        link = chrome.find_element_by_link_text('CSV 下載')
        link.click()
    except:
        print("股號:{} 無法下載.".format(stockNum))
        break    
    time.sleep(2)
    chrome.close()
    

chrome.quit()
TRACK_UpdateData.CalData()