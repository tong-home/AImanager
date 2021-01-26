#coding:utf-8
from selenium import webdriver
import os,time,HTMLTestRunner
driver=webdriver.Chrome()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

###登录###
driver.get('http://t-ucenter.brandwisdom.cn/login')
driver.maximize_window()
driver.find_element_by_name("username").send_keys('wangmm@jointwisdom.cn')
driver.find_element_by_name("password").send_keys('Mm123456')
driver.find_element_by_id("newLogin").click()
driver.implicitly_wait(30)
try:
    #关闭弹窗
    driver.find_element_by_class_name('bs-spidemic-close').click()
    driver.find_element_by_class_name('bs-spidemic-button').click()

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

driver.find_element_by_class_name('bs-header-hotel-list-title').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div/div[2]/div[3]').click()
time.sleep(3)


 # 点击进入客需设置页面
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div').click()
driver.find_element_by_css_selector('#root > div.ai-menu > div > div > div.center > div > div:nth-child(4) > div.bs-transition > div > div:nth-child(3) > div > div > div').click()
driver.implicitly_wait(30)

driver.find_element_by_class_name('zent-switch-small.zent-switch-checked.zent-switch').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/button[1]').click()


'''
####----开票服务的关闭和开通----####
driver.find_element_by_css_selector('[data-key="9"]').click()
time.sleep(1)
driver.find_element_by_class_name('zent-switch-small.zent-switch-checked.zent-switch').click()
time.sleep(1)
driver.find_element_by_xpath("//div[@class='JW_Service_close-dialog-footer']/button[@class='zent-btn-primary zent-btn']").click()

###开通开票服务
driver.find_element_by_class_name('zent-switch-small.zent-switch').click()
driver.find_element_by_class_name('zent-select-text').click()
time.sleep(1)
# 选择女子会所为转接部门
driver.find_element_by_css_selector('span[value="11"]').click()
time.sleep(1)

above=driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div.JW-C-form-item.JW-C-form-item_block.JW_Service_open-label > div.JW-C-form-control > div > input')
ActionChains(driver).move_to_element(above).perform()
ActionChains(driver).click(above).perform()
time.sleep(1)
os.system("D:\\AImanager\\base\\Autolt\\upload.exe")
time.sleep(2)
driver.find_element_by_xpath('//*[@class="JW_material-detail-footer"]/button[1]').click()
time.sleep(2)

# 点击创建流程(节点名称为开票1并点击保存并使用)
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div/div').click()
driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.module-container.JW_P_nodes > div > div:nth-child(2) > div > div > input').send_keys(u'开票1')
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/label[1]/span[1]/input').click()
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/h3/button[1]/span').click()
invoice=driver.find_element_by_css_selector('span[title="开票1"]').text
print('invoice是：',invoice)
if(invoice=="开票1"):
    print('正确')
else:
    print('失败')

# 测试完成后点击进入产品中心
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
#driver.quit()
'''
