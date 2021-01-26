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

class Service(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "https://t-ucenter.brandwisdom.cn/login"
    verificationErrors = []
    accept_next_alert = True
    driver.get(base_url)
    driver.maximize_window()
    driver.find_element_by_name("username").send_keys('13340113147@163.com')
    driver.find_element_by_name("password").send_keys('Mm123456')
    driver.find_element_by_id("newLogin").click()
    # driver.implicitly_wait(30)
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

    def test_invoice(self):
        driver = self.driver

        # 点击进入客需设置页面
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div').click()
        driver.find_element_by_css_selector(
            '#root > div.ai-menu > div > div > div.center > div > div:nth-child(4) > div.bs-transition > div > div:nth-child(3) > div > div > div').click()
        time.sleep(1)

        ####----开票服务的关闭和开通----####
        #1、电话服务方式：语音播报+有二维码
        #2、电话服务方式：转接人工+有二维码
        ##关闭开票服务
        driver.find_element_by_css_selector('[data-key="9"]').click()
        time.sleep(1)
        driver.find_element_by_class_name('zent-switch-small.zent-switch-checked.zent-switch').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//div[@class='JW_Service_close-dialog-footer']/button[@class='zent-btn-primary zent-btn']").click()
        time.sleep(1)

        ###开通开票服务(选择自动的语音播报)
        driver.find_element_by_class_name('zent-switch-small.zent-switch').click()
        time.sleep(1)
        # 选择开票二维码
        above = driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div.JW-C-form-item.JW-C-form-item_block.JW_Service_open-label > div.JW-C-form-control > div > input[type=file]')
        ActionChains(driver).move_to_element(above).perform()
        ActionChains(driver).click(above).perform()
        time.sleep(1)
        os.system("D:\\AImanager\\base\\Autolt\\upload.exe")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@class="zent-dialog-r-footer"]/button[1]').click()
        time.sleep(2)

        ##再次关闭开票服务（电话服务方式：转接人工，部门为女子会所）
        driver.find_element_by_css_selector('[data-key="9"]').click()
        time.sleep(1)
        driver.find_element_by_class_name('zent-switch-small.zent-switch-checked.zent-switch').click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='JW_Service_close-dialog-footer']/button[@class='zent-btn-primary zent-btn']").click()
        time.sleep(1)

        ###开通开票服务(选择转接人工，转接部门为女子会所)
        driver.find_element_by_class_name('zent-switch-small.zent-switch').click()
        time.sleep(1)
        driver.find_element_by_css_selector("body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div:nth-child(1) > div.zent-popover-wrapper.zent-select > div").click()
        time.sleep(1)
        # 电话服务方式选择为转接人工
        driver.find_element_by_css_selector('span[value="2"]').click()
        time.sleep(1)
        #电话转接部门选择为女子会所
        driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div:nth-child(2) > div.zent-popover-wrapper.zent-select > div').click()
        driver.find_element_by_css_selector('span[value="11"]').click()
        #选择开票二维码
        above = driver.find_element_by_css_selector(
            'body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div.JW-C-form-item.JW-C-form-item_block.JW_Service_open-label > div.JW-C-form-control > div > input[type=file]')
        ActionChains(driver).move_to_element(above).perform()
        ActionChains(driver).click(above).perform()
        time.sleep(1)
        os.system("D:\\AImanager\\base\\Autolt\\upload.exe")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@class="zent-dialog-r-footer"]/button[1]').click()
        time.sleep(2)

        # 点击创建流程(节点名称为开票1并点击保存并使用)
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div/div').click()
        driver.find_element_by_css_selector(
            '#root > div.ai-container > div.ai-content > div.module-container.JW_P_nodes > div > div:nth-child(2) > div > div > input').send_keys(
            u'开票1')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/label[1]/span[1]/input').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/h3/button[1]/span').click()
        invoice = driver.find_element_by_css_selector('span[title="开票1"]').text
        self.assertEqual(invoice,"开票1")



    #关闭并开通加床服务用例
    def test_bed(self):
        driver = self.driver
        # 点击进入客需设置页面
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div').click()
        driver.find_element_by_css_selector('#root > div.ai-menu > div > div > div.center > div > div:nth-child(4) > div.bs-transition > div > div:nth-child(3) > div > div > div').click()
        time.sleep(2)

        # 点击关闭加床服务
        driver.find_element_by_css_selector('[data-key="15"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[3]/div[1]/span[1]/span').click()
        driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div.JW_Service_close-dialog-footer > button.zent-btn-primary.zent-btn').click()
        time.sleep(1)

        # 点击开通加床服务，选择转接部门为spa
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[3]/div/span/span').click()
        driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div:nth-child(2) > div.zent-popover-wrapper.zent-select > div').click()
        driver.find_element_by_css_selector('span[value="7"]').click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/button[1]").click()

        # 加床服务创建流程
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div/div/a').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div/div/input').send_keys(u'加床1')
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/label[1]/span[1]/input').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/h3/button[1]/span').click()


    def test_morning_call(self):
        driver = self.driver
        # 点击进入客需设置页面
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[2]/div/div').click()
        driver.find_element_by_css_selector('#root > div.ai-menu > div > div > div.center > div > div:nth-child(4) > div.bs-transition > div > div:nth-child(3) > div > div > div').click()
        time.sleep(1)

        ####----叫醒服务的关闭和开通----####
        #1、叫醒服务选择 转接人工 服务方式
        #2、叫醒服务选择 自动下单 服务方式

        #关闭叫醒服务
        driver.find_element_by_css_selector('[data-key="8"]').click()
        driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.module-container.JW_P_sersetting > div.module-container.JW_P_sersetting-serviceContainer.JW_P_sersetting-clean > div.service-list > span.service-item > span.zent-switch-small.zent-switch-checked.zent-switch').click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='JW_Service_close-dialog-footer']/button[@class='zent-btn-primary zent-btn']").click()

        ###开通叫醒服务--服务方式为默认的转接人工
        driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.module-container.JW_P_sersetting > div.module-container.JW_P_sersetting-serviceContainer.JW_P_sersetting-clean > div > span.service-item > span').click()
        driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div:nth-child(2) > div.zent-popover-wrapper.zent-select > div').click()
        time.sleep(1)
        # 选择中餐厅为转接部门电话
        driver.find_element_by_css_selector('span[value="8"]').click()
        driver.find_element_by_css_selector("body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-footer > button.zent-btn-primary.zent-btn").click()
        time.sleep(1)

        #关闭叫醒服务
        driver.find_element_by_css_selector('[data-key="8"]').click()
        driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.module-container.JW_P_sersetting > div.module-container.JW_P_sersetting-serviceContainer.JW_P_sersetting-clean > div.service-list > span.service-item > span.zent-switch-small.zent-switch-checked.zent-switch').click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='JW_Service_close-dialog-footer']/button[@class='zent-btn-primary zent-btn']").click()

        ###开通叫醒服务--服务方式为自动下单
        driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.module-container.JW_P_sersetting > div.module-container.JW_P_sersetting-serviceContainer.JW_P_sersetting-clean > div > span.service-item > span').click()
        driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div:nth-child(1) > div.zent-popover-wrapper.zent-select > div').click()
        time.sleep(1)
        # 选择中餐厅为转接部门电话
        driver.find_element_by_css_selector('span[value="1"]').click()

        driver.find_element_by_css_selector('body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-body > div:nth-child(2) > div.zent-popover-wrapper.zent-select > div').click()
        time.sleep(1)
        # 选择中餐厅为转接部门电话
        driver.find_element_by_css_selector('span[value="8"]').click()
        driver.find_element_by_css_selector("body > div.zent-portal.zent-dialog-r-anchor > div > div.zent-dialog-r-wrap > div > div.zent-dialog-r-footer > button.zent-btn-primary.zent-btn").click()
        time.sleep(1)


        # 点击创建流程(节点名称为叫醒1并点击保存并使用)
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div/div/a').click()
        driver.find_element_by_css_selector('#root > div.ai-container > div.ai-content > div.module-container.JW_P_nodes > div > div:nth-child(2) > div > div > input').send_keys(u'叫醒1')
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/label[1]/span[1]/input').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/h3/button[1]/span').click()

        # 登录成功后点击进入产品中心
        #driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div[1]/a/div').click()
        driver.quit()

    def tearDown(self):
        #self.driver.quit()
        driver = self.driver

'''
if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()
    #将测试用例，加入到测试容器中
    test.addTest(Service("test_bed"))
    test.addTest(Service("test_morning_call"))
    test.addTest(Service("test_invoice"))

    #  设置报告文件保存路径
    report_path =  'D:\\AImanager\\base\\Result\\'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #  设置报告名称格式
    HtmlFile = report_path + now + "服务关闭和开通.html"
    print(HtmlFile)
    #  python3.0不支持file函数，可以用open()来替代
    file_result = open(HtmlFile, "wb")  # 写入

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"AI管家服务关闭和开通", description = u"用例执行情况")

    #运行测试用例
    runner.run(test)
    file_result.close()
'''