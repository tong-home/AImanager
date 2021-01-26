#coding:utf-8
#引入webdriver和unittest所需要的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#引入HTMLTestRunner包
import HTMLTestRunner

class Login(unittest.TestCase):
    #初始化设置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://dv-ucenter.brandwisdom.cn/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    #BW登录
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_name("username").send_keys('tongtong.mu@jointwisdom.cn')
        driver.find_element_by_name("password").send_keys('MTT2019')
        driver.find_element_by_id("newLogin").click()
        driver.implicitly_wait(30)
        time.sleep(6)
        a = driver.title
        self.assertEqual(a, 'AI管家')
        '''
        if (a == '产品中心'):
            time.sleep(2)
            # 滚动条滚动到页面最下方
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector(
                "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
            time.sleep(2)
            a1 = driver.title
            self.assertEqual(a1, 'AI管家')
            #先返回产品中心
            driver.find_element_by_css_selector(
                '#root > div.ai-container > div.ai-header > div > div > div.bs-header-option > div.bs-header-menu-list > a > div').click()
            # 滚动条滚动到页面最下方
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector(
                "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_box_2zANd > div > div").click()
            time.sleep(2)
            a2 = driver.title
            self.assertEqual(a2, 'AI管家')
        else:
            # 不是产品中心先返回产品中心
            driver.find_element_by_css_selector('#root > div.ai-container > div.ai-header > div > div > div.bs-header-option > div.bs-header-menu-list > a > div').click()
            # 滚动条滚动到页面最下方
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector(
                "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
            time.sleep(2)
            a1 = driver.title
            # self.assertEqual(a1, 'AI管家')
            # 不是产品中心先返回产品中心
            driver.find_element_by_css_selector(
                '#root > div.ai-container > div.ai-header > div > div > div.bs-header-option > div.bs-header-menu-list > a > div').click()
            # 滚动条滚动到页面最下方
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector(
                "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_box_2zANd > div > div").click()
            time.sleep(2)
            a2 = driver.title
            self.assertEqual(a2, 'AI管家')
        # 登录成功后点击进入产品中心
        '''
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
    def tearDown(self):
        self.driver.quit()
"""
if __name__ == "__main__":
    import os
    #定义一个测试容器
    suite = unittest.TestSuite()
    #将测试用例，加入到测试容器中
    suite.addTest(Login("test_login"))
    #  设置报告文件保存路径
    report_path = '/Users/mtt/PycharmProjects/AImanager/base/Result'
    #report_path = '../Result'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(now)
    #  设置报告名称格式
    HtmlFile = os.path.join(report_path,"登录.html")
    #print(HtmlFile)
    #  python3.0不支持file函数，可以用open()来替代
    file_result = open(HtmlFile,"wb")
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"AI管家登录测试", description = u"用例执行情况")
    #运行测试用例
    runner.run(suite)
    file_result.close()
"""