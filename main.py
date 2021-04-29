# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
URL = 'https://www.acmicpc.net/ranklist'

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(url=URL)

itme_cnt = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[3]/div[3]/div/table/tbody/tr')
print(len(itme_cnt))
for i in range(100):
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[3]/div/table/tbody/tr[' + str(i+1) +']/td[2]/a').click()
    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')
    selector = soup.find(id="u-solved")
    print(selector)
    driver.back()