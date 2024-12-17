import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd

def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

def main():
    driver = driver()
    print('웹 드라이버 연결완료 !')

def driver_connection(driver ,path):
    # 크롬 드라이버 생성
    driver.get(path)

def execute_script(driver, script):
    driver.execute_script(script)

def wb_wait(driver, time, by, target):
    #target : 'id'
    wd(driver, time).until(EC.presence_of_element_located((by, target)))

def click(type, name):
    btn = driver.find_element(type, name)
    btn.click()

if __name__ == "__main__" :
    main()