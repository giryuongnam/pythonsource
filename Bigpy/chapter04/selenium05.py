from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options=Options()
s=Service("C:/source/pythonsource/Bigpy/Py_scrap/chromedriver/chromedriver.exe")

driver=webdriver.Chrome(service=s, options=chrome_options)

driver.set_window_size(1920,1080) # 화면크기
driver.get('https://google.com')
time.sleep(3) # 대기(모든 load 1초가 걸려도 3초 기다림)
driver.save_screenshot("C:/source/pythonsource/Bigpy/Py_scrap/img/Website3.png")

driver.set_window_size(1920,1080)
driver.get('https://daum.net')
time.sleep(3)
driver.save_screenshot("C:/source/pythonsource/Bigpy/Py_scrap/img/Website4.png")

driver.quit()

print('스크린샷 성공')

