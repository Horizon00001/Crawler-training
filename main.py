from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep
from random import uniform
from pathlib import Path

def press_sign_button():
    pic_addr = str(Path(__file__).parent / 'login.png')
    #pic_addr = 'C:/Users/LENOVO/Desktop/crawl/login.png'
    loc = pyautogui.locateOnScreen(pic_addr)
    p = pyautogui.center(loc)
    pyautogui.moveTo(p)
    pyautogui.leftClick()

def login():

    wd = Chrome()
    wd.get('https://www.douban.com/')
    sleep(5)

    iframe = wd.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
    sleep(2)
    wd.switch_to.frame(iframe)   
    wd.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click()

    sleep(uniform(1,4))
    wd.find_element(By.XPATH, '//*[@id="username"]').send_keys('15223539257')
    sleep(uniform(1,4))
    wd.find_element(By.XPATH, '//*[@id="password"]').send_keys('Zj123456789')
    #sleep(uniform(1,4))
    #wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    sleep(10)

    yanzhengma_iframe = wd.find_element(By.XPATH, '//*[@id="tcaptcha_iframe_dy"]')
    sleep(2)
    wd.switch_to.frame(yanzhengma_iframe)

    


login()
press_sign_button()

sleep(10000000)
