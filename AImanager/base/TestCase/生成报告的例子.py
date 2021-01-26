# -*- coding: utf-8 -*-
#引入webdriver和unittest所需要的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

#引入HTMLTestRunner包
import HTMLTestRunner
'''

class Baidu(unittest.TestCase):
    #初始化设置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium Webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()

    #将测试用例，加入到测试容器中
    test.addTest(Baidu("test_baidu"))

    #定义个报告存放的路径，支持相对路径
    #file_path = 'E:/工作文档/2019/AI manager/case/base/Result/report.html'
    #file_result = open(file_path, 'wb')
    #  设置报告文件保存路径
    report_path = os.path.dirname(os.path.abspath('.')) + '/Result/'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #  设置报告名称格式
    HtmlFile = report_path + now + "HTMLtemplate.html"
    print(HtmlFile)
    #  python3.0不支持file函数，可以用open()来替代
    # file_result = file(HtmlFile, "wb")
    file_result = open(HtmlFile, "wb")  # 写入


    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"百度搜索测试报告", description = u"用例执行情况")

    #运行测试用例
    runner.run(test)
    file_result.close()
'''

with open('cookies', 'r', encoding='utf-8') as f:
    list_cookies = json.loads(f.readline())
    print(list_cookies)
    # cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
    # cookiestr = '; '.join(item for item in cookie)
    # print(cookiestr)

    driver.get("https://jd.com")
    driver.delete_all_cookies()

    for cookie in list_cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    driver.get("https://order.jd.com/center/list.action")
    #return driver


