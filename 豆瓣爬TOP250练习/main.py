from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import csv

def isElement_exist(wd):
    try:
        wd.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div[2]/span[3]/a')
        return True
    except:
        return False
    
myoptions = ChromeOptions()
myoptions.add_argument('--headless')

csvfile = open('csv豆瓣top250.csv', 'w', encoding='utf-8', newline='')
writer_obj = csv.writer(csvfile)
writer_obj.writerow(['排名', '名称'])

wd = Chrome(options=myoptions)

wd.get('https://movie.douban.com/top250?start=0&filter=')
sleep(1)


while True:
    li_list = wd.find_elements(By.XPATH,'//*[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/ol[@class="grid_view"]/li')
    for li in li_list:
        num = li.find_element(By.XPATH,'./div[@class="item"]/div[@class="pic"]/em').text

        name = li.find_element(By.XPATH,'./div[@class="item"]/div[@class="info"]/div[@class="hd"]/a').text
        print(num,name)
        data_list = []
        data_list.append(num)
        data_list.append(name)
        writer_obj.writerow(data_list)
        
    if isElement_exist(wd) == True:
        wd.find_element(By.XPATH, '//*[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/div[@class="paginator"]/span[@class="next"]/a').click()
        sleep(1)
    else:
        break

wd.quit()

