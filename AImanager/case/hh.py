# coding = utf-8

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://blog.csdn.net/morling05/article/details/81094151')
print(driver.title)

driver.quit()