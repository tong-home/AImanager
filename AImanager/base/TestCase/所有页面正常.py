#coding:utf-8
from selenium import webdriver
import os,time,HTMLTestRunner
driver=webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

###登录###
driver.get('http://dv-ucenter.brandwisdom.cn/login')
driver.maximize_window()
driver.find_element_by_name("username").send_keys('wangmm@jointwisdom.cn')
driver.find_element_by_name("password").send_keys('Mm123456')
driver.find_element_by_id("newLogin").click()
driver.implicitly_wait(30)
try:
    #关闭弹窗
    driver.find_element_by_class_name('bs-spidemic-close').click()
except:
    time.sleep(1)
title=driver.title
if(title=='产品中心'):
    # 滚动条滚动到页面最下方
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    driver.find_element_by_css_selector("#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
    time.sleep(2)
else:
    #不是产品中心先返回产品中心
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
    # 滚动条滚动到页面最下方
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    driver.find_element_by_css_selector("#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
    time.sleep(2)

#点击进入客需设置页面进入员工登记页面【需要先手动添加角色】
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div').click()
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div').click()
#time.sleep(1)






#测试完成后点击进入产品中心
#driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
#driver.quit()

