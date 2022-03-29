from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import mergeFile
stockNums = input("輸入要下載的股號(可批量下載)：")
try:
    totalyear = int(input("輸入要下載幾年(初始為1年)："))
except:
    totalyear = 1

print('下載股號為：',stockNums.split(' '))
for stockNum in stockNums.split(' '):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\KK\\Desktop\\data\\stock_data\\'+str(stockNum)}
    options.add_experimental_option('prefs', prefs)
    chrome = webdriver.Chrome('./chromedriver',options = options)
    chrome.get("https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html")

    Typein = chrome.find_element_by_name("stockNo")
    s1 = Select(chrome.find_element_by_name('yy'))
    s2 = Select(chrome.find_element_by_name('mm'))
    Typein.send_keys(stockNum)

    year = 0
    for select1 in s1.options:
        if (year==totalyear):
            break
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
        year+=1
    chrome.close()

chrome.quit()
mergeFile.mergeFiles(stockNums)
