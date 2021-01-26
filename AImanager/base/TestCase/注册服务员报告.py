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


class Waiter(unittest.TestCase):
    #初始化设置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://t-ucenter.brandwisdom.cn/login"
        self.verificationErrors = []
        self.accept_next_alert = True


    #服务员
    def test_waiter(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_name("username").send_keys('13340113147@163.com')
        driver.find_element_by_name("password").send_keys('Mm123456')
        driver.find_element_by_id("newLogin").click()
        driver.implicitly_wait(30)
        time.sleep(6)

        title = driver.title
        if (title == '产品中心'):
            # 滚动条滚动到页面最下方
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector(
                "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
            time.sleep(2)
        else:
            # 不是产品中心先返回产品中心
            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
            # 滚动条滚动到页面最下方
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector(
                "#root > div.root-wraper > div > div > div.container_1uIxv > div:nth-child(3) > div.product_item_itm_3KCoy > div > div.item_body_hsn6- > div.item_body_entry_7ZTEa").click()
            time.sleep(2)
        # 点击进入客需设置页面进入员工登记页面【需要先手动添加角色】
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div/div/div').click()
        time.sleep(1)

        #####查找电话为15611322762的服务员,查到后删除，没查到直接新增####
        # 点击筛选电话号码并点击确定
        driver.find_element_by_name('phoneNo').send_keys('15611322762')
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(2)
        try:
            phone1 = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[3]/span').text
            if (phone1 == "15611322762"):
                # 点击删除已经存在的服务员
                driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]/span[2]').click()
                time.sleep(1)
            else:
                time.sleep(1)
        except:
            time.sleep(1)


        #####新增电话为15611322762的服务员####

        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(1)
        driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.JW_waiter-page > div > button').click()
        time.sleep(1)

        # 点击输入名称为Auto
        name = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/div/div/input')
        ActionChains(driver).move_to_element(name).perform()
        ActionChains(driver).click(name).perform()
        ActionChains(driver).send_keys('Auto').perform()
        # 点击输入电话
        phone = driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[3]/div/div/input')
        ActionChains(driver).move_to_element(phone).perform()
        ActionChains(driver).click(phone).perform()
        ActionChains(driver).send_keys('15611322762').perform()

        ##点击选择角色
        action = driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td[4]/div/div/div')
        ActionChains(driver).move_to_element(action).perform()
        ActionChains(driver).click(action).perform()
        #不同酒店选择的角色不一样
        driver.find_element_by_css_selector('span[value="69"]').click()
        time.sleep(1)
        # 点击保存按钮
        driver.find_element_by_class_name('gridHandleCol.primary').click()
        time.sleep(2)
        #  设置报告文件保存路径
        png_path = 'D:\\AImanager\\base\\Image\\'
        #  获取系统当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #  设置报告名称格式
        Pngname = now + "注册服务员"
        # 网页截图并保存
        driver.get_screenshot_as_file(png_path + Pngname + ".png")

        # 登录成功后点击进入产品中心
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()


    def tearDown(self):
        #self.driver.quit()
        driver=self.driver
        driver.quit()

'''
if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()

    #将测试用例，加入到测试容器中
    test.addTest(Waiter("test_waiter"))
    #  设置报告文件保存路径
    report_path =  'D:\\AImanager\\base\\Result\\'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #  设置报告名称格式
    HtmlFile = report_path + now + "删除并服务员.html"
    #print(HtmlFile)
    #  python3.0不支持file函数，可以用open()来替代
    file_result = open(HtmlFile,"wb")

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"AI管家注册服务员测试", description = u"用例执行情况")
    #运行测试用例
    runner.run(test)
    file_result.close()
'''