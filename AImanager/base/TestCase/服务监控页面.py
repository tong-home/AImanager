#coding:utf-8
from selenium import webdriver
import os,time,HTMLTestRunner
import unittest
driver=webdriver.Chrome()


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

#点击进入服务监控页面并新增
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div').click()
driver.find_element_by_xpath('//*[@class="tab-container"]/button[@class="zent-btn-primary zent-btn"]').click()

#选择叫醒服务类型
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element_by_css_selector('span[value="8"]').click()
#选择楼层
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
#选择叫醒服务的预约时间为2020-12-08
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/span[2]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/div[2]/div/ul[4]/li[3]/div').click()
driver.find_element_by_css_selector('div.date-panel > div.date-table.panel-table > div > ul:nth-child(5) > li:nth-child(5) > div[title="2020-12-31"]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()

shi2= time.strftime("%m/%d %H:%M", time.localtime(time.time()))
time.sleep(1)
#获取toast内容
a=driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text

#  设置报告文件保存路径
png_path = 'E:\\工作文档\\2019\\AI manager\\case\\base\\Image\\'
#  获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#  设置报告名称格式
Pngname =now+"叫醒"
hh=print('查看路径',png_path+Pngname)
#网页截图并保存
driver.get_screenshot_as_file(png_path+Pngname+".png")

#查询到叫醒服务
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element_by_css_selector('span[value="8"]').click()
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
shi1=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[3]/div/div/table/tbody/tr[1]/td[6]/span').text
print('shi1',shi1)
print('shi2',shi2)
if (shi1 ==shi2):
    print(u"测试成功，结果和预期结果匹配！")
else:
    print(u"测试失败，结果和预期结果不一致！")


'''
#选择加床服务类型
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element_by_css_selector('span[value="15"]').click()
#选择楼层
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()
time.sleep(1)
shi2= time.strftime("%m/%d %H:%M", time.localtime(time.time()))
#获取toast内容
a=driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text

print(u'获取的文字为：',a)
if (a == '增加成功'):
    print(u"测试成功，结果和预期结果匹配！")
else:
    print(u"测试失败，结果和预期结果不一致！")

#  设置报告文件保存路径
png_path = 'E:\\工作文档\\2019\\AI manager\\case\\base\\Image\\'
#  获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#  设置报告名称格式
Pngname =now+"加床"
hh=print('查看路径',png_path+Pngname)
#网页截图并保存
driver.get_screenshot_as_file(png_path+Pngname+".png")

#查询到加床服务
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element_by_css_selector('span[value="15"]').click()
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
shi1=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[3]/div/div/table/tbody/tr[1]/td[6]/span').text
print('shi1',shi1)

print('shi2',shi2)
if (shi1 ==shi2):
    print(u"测试成功，结果和预期结果匹配！")
else:
    print(u"测试失败，结果和预期结果不一致！")

'''

#登录成功后点击进入产品中心
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
#driver.quit()


