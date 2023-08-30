from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service(executable_path=r"C:\Users\FutureCode\Downloads\chromedriver-win64\chromedriver.exe")

browser = webdriver.Chrome(service = service)

try:
    browser.get('https://belluna.ru/test-signup')    
    phone = browser.find_element(By.NAME, 'Phone')
    phone.send_keys("88005553535")
    email = browser.find_element(By.NAME, 'Email')
    email.send_keys("hjhjhjh@gmail.com")
    name = browser.find_element(By.NAME, 'Name')
    name.send_keys("Компьютер")
    сomments = browser.find_element(By.NAME, 'Comments')
    сomments.send_keys("Этот текст написал компьютер")
    button = browser.find_element(By.CLASS_NAME, 't-submit')
    button.click()
    print(1)
    
    time.sleep(10)
    browser.quit()
except:
    print(2)
    
nav-item nav-link