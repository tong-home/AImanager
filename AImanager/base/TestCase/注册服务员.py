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




#点击筛选电话号码并点击确定
driver.find_element_by_name('phoneNo').send_keys('15611322762')
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/button').click()
time.sleep(1)
try:
    phone1=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[3]/span').text
    print('dianhua:',phone1)
    if(phone1=="15611322762"):
        print('pass')
        # 点击删除已经存在的服务员
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]/span[2]').click()
        time.sleep(1)
    else:
        time.sleep(1)
except:
    time.sleep(1)


#新增用户18518053025,点击新增按钮
driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.JW_waiter-page > div > button').click()
time.sleep(1)

#点击输入名称为Auto
name=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/div/div/input')
ActionChains(driver).move_to_element(name).perform()
ActionChains(driver).click(name).perform()
ActionChains(driver).send_keys('Auto').perform()
#点击输入电话
phone=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[3]/div/div/input')
ActionChains(driver).move_to_element(phone).perform()
ActionChains(driver).click(phone).perform()
ActionChains(driver).send_keys('15611322762').perform()

##点击选择角色
action=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[4]/div/div/div')
ActionChains(driver).move_to_element(action).perform()
ActionChains(driver).click(action).perform()
driver.find_element_by_css_selector('span[value="1"]').click()
time.sleep(1)
#点击保存按钮
driver.find_element_by_class_name('gridHandleCol.primary').click()
time.sleep(2)



