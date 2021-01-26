#coding:utf-8
from selenium import webdriver
#import os,time,HTMLTestRunner
import time
driver=webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains
###登录###
driver.get('https://dv-ucenter.brandwisdom.cn/login')
driver.maximize_window()
driver.find_element_by_name("username").send_keys('tongtong.mu@jointwisdom.cn')
driver.find_element_by_name("password").send_keys('MTT2019')
driver.find_element_by_id("newLogin").click()
driver.implicitly_wait(30)
time.sleep(6)
title=driver.title
print('title是多少：：：',title)
if(title=='产品中心'):
    time.sleep(1)
    # 滚动条滚动到页面最下方
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    #点击AI管家中的‘进入’
    driver.find_element_by_css_selector("#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
    time.sleep(2)
    #判断登录的title是否是AI管家
    a1=driver.title
    time.sleep(1)
    # 先返回产品中心
    driver.find_element_by_css_selector(
        '#root > div.ai-container > div.ai-header > div > div > div.bs-header-option > div.bs-header-menu-list > a > div').click()
    # 滚动条滚动到页面最下方
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    #点击AI管家的‘进入系统’
    driver.find_element_by_css_selector(
        "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_box_2zANd > div > div").click()
    time.sleep(2)
    a2 = driver.title
    #self.assertEqual(a2, 'AI管家')

else:
    #不是产品中心先返回产品中心
    driver.find_element_by_css_selector('#root > div.ai-container > div.ai-header > div > div > div.bs-header-option > div.bs-header-menu-list > a > div').click()
    # 滚动条滚动到页面最下方
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    #点击AI管家的‘进入’
    driver.find_element_by_css_selector("#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
    time.sleep(2)
    a1 = driver.title
    #self.assertEqual(a1, 'AI管家')
    #先返回产品中心
    driver.find_element_by_css_selector('#root > div.ai-container > div.ai-header > div > div > div.bs-header-option > div.bs-header-menu-list > a > div').click()
    # 滚动条滚动到页面最下方
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    #点击AI管家的‘进入系统’
    driver.find_element_by_css_selector(
        "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_box_2zANd > div > div").click()
    time.sleep(2)
    a2 = driver.title
    if(a2=='AI管家'):
        print('通过')
    #self.assertEqual(a2, 'AI管家')

driver.quit()


