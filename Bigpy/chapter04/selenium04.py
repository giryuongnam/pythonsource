from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options=Options()
s=Service("C:/source/pythonsource/Bigpy/Py_scrap/chromedriver/chromedriver.exe")

driver=webdriver.Chrome(service=s, options=chrome_options)

driver.get('https://google.com')
driver.save_screenshot("C:/source/pythonsource/Bigpy/Py_scrap/img/Website1.png")

driver.get('https://daum.net')
driver.save_screenshot("C:/source/pythonsource/Bigpy/Py_scrap/img/Website2.png")

driver.quit()

print('스크린샷 성공')