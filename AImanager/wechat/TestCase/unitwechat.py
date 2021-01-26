import os, time
import unittest
from appium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait


class Open(unittest.TestCase):
    # Returns abs path relative to this file and not cwd
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

    desired_cap = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "VBJDU18809000980",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": "True",
        "fullReset": "False",
        "fastReset": "False",
        "newCommandTimeout": "10",
        "resetKeyboard": "True",
        "unicodeKeyboard": "True",
        "chromeOptions": {"androidProcess": "com.tencent.mm:tools"}

    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

    # 这里设置智能等待10s
    driver.implicitly_wait(10)
    # 进入微信后点击搜索，并输入公众号的名字->点击[微信有机制，这两个值会定期变动]
    el1 = driver.find_element_by_id("com.tencent.mm:id/f8y")
    el1.click()
    el2 = driver.find_element_by_id("com.tencent.mm:id/bhn")
    ###测试环境的账号###
    #el2.send_keys("wangmingming3147")
    #driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'wangmingming3147的接口测试号')]").click()
    ###生产环境的账号###
    el2.send_keys("酒店AI管家")
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'酒店AI管家')]").click()
    time.sleep(1)
    driver.get_screenshot_as_file('D:/AImanager/wechat/Image/进入公众号.png')

    def test_menu(self):
        driver=self.driver
        driver.find_element_by_android_uiautomator('new UiSelector().text("上班设置")').click()
        driver.get_screenshot_as_file('D:/AImanager/wechat/Image/上班设置.png')
        time.sleep(1)
        driver.back()

        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        driver.get_screenshot_as_file('D:/AImanager/wechat/Image/个人中心.png')
        time.sleep(1)
        driver.back()

        driver.find_element_by_android_uiautomator('new UiSelector().text("客需管理")').click()
        time.sleep(1)

    def test_createwu(self):
        # *************************##
        # 点击新增-创建送物客需任务
        # *************************
        driver = self.driver
        driver.switch_to.context('WEBVIEW_xweb')
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[3]/a'))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[3]/a').click()
        time.sleep(1)

        # 选择服务类型-送物服务
        driver.find_element_by_class_name('am-list-line').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div[1]/div/div[1]/span[2]').click()

        # 选择楼层
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div[1]/div/div[1]/span[2]').click()
        time.sleep(1)

        # 选择第一个物品
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[5]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/a').click()

        # 直接下单
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/a[2]').click()
        WebDriverWait(driver, 2).until(
            lambda driver: driver.find_element_by_class_name('am-toast-text-info'))
        a = driver.find_element_by_class_name('am-toast-text-info').text

        #if (a == '新增成功'):
            #print('成功')
        self.assertEqual(a, '新增成功')

    def test_createsao(self):

        # *************************##
        # 点击新增-创建打扫服务的客需任务
        # *************************##
        driver=self.driver
        time.sleep(1)
        driver.switch_to.context('WEBVIEW_xweb')
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[3]/a'))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[3]/a').click()
        time.sleep(1)

        #print(driver.contexts)
        # 选择服务类型-打扫服务
        driver.find_element_by_class_name('am-list-line').click()
        time.sleep(1)
        # 向上滑动屏幕选中打扫服务
        # driver.find_element_by_xpath('am-picker-col-indicator ').click()
        driver.switch_to.context('NATIVE_APP')
        time.sleep(1)
        driver.swipe(829.2, 1482.3, 820.2, 1390.4, 500)
        time.sleep(1)
        driver.switch_to.context('WEBVIEW_xweb')
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div[1]/div/div[1]/span[2]').click()

        # 选择楼层
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div[1]/div/div[1]/span[2]').click()
        time.sleep(1)

        # 直接下单
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/a[2]').click()
        WebDriverWait(driver, 2).until(
            lambda driver: driver.find_element_by_class_name('am-toast-text-info'))
        a = driver.find_element_by_class_name('am-toast-text-info').text
        #if (a == '新增成功'):
            #print('成功')
        self.assertEqual(a,'新增成功')

    def test_page(self):
        driver = self.driver
        time.sleep(3)
        driver.switch_to.context('WEBVIEW_xweb')
        #  获取系统当前时间
        now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(driver.current_context)
        ####测试各个状态 的页面能正常点击并切换
        # 点击已受理，进入已受理页面
        time.sleep(1)
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[2]'))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[2]').click()
        time.sleep(1)
        # 点击已完成，进入已完成页面
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[3]').click()
        time.sleep(1)
        driver.switch_to.context('NATIVE_APP')
        driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="containerFrameLayout"]/android.widget.FrameLayout/android.widget.FrameLayout').click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.switch_to.context('WEBVIEW_xweb')
        time.sleep(1)
        # 点击已取消，进入已完成页面
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[4]').click()
        time.sleep(1)
        driver.switch_to.context('NATIVE_APP')
        driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="containerFrameLayout"]/android.widget.FrameLayout/android.widget.FrameLayout').click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.switch_to.context('WEBVIEW_xweb')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]').click()
        time.sleep(1)

    def test_acceptaccept(self):
        ##********************************************************************##
        # 点击进入详情页面，点击受理+完成
        ##********************************************************************##
        driver = self.driver
        driver.switch_to.context('WEBVIEW_xweb')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]').click()
        # 点击进入详情页面，点击受理+完成【列表页除了页签外，其他的webview名字为：'NATIVE_APP'的】
        time.sleep(1)
        driver.switch_to.context('NATIVE_APP')
        driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="containerFrameLayout"]/android.widget.FrameLayout/android.widget.FrameLayout').click()
        # print('详情页面的webview:',driver.current_context)
        time.sleep(1)
        # driver.back()
        # 点击受理【详情页面是名字为'WEBVIEW_xweb'的webview中】
        driver.switch_to.context('WEBVIEW_xweb')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[6]/a[2]').click()
        time.sleep(1)
        # 点击完成
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[6]/a[3]').click()
        # 点击链接进入微信公众号之后，需要切换上下文（webview），如果不能理解，则可以把他看成Iframe
        time.sleep(1)
        driver.back()

    def test_acceptcancel(self):
        ##********************************************************************##
        # 点击进入详情页面，点击受理+取消
        ##********************************************************************##
        driver=self.driver
        # 点击进入详情页面，点击受理+取消【列表页除了页签是在'WEBVIEW_xweb'，其他都是在：'NATIVE_APP'】
        driver.switch_to.context('WEBVIEW_xweb')
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]'))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]').click()
        # 点击进入详情页面，点击受理+完成【列表页除了页签外，其他的webview名字为：'NATIVE_APP'的】
        driver.switch_to.context('NATIVE_APP')
        time.sleep(1)
        driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="containerFrameLayout"]/android.widget.FrameLayout/android.widget.FrameLayout').click()
        # print('详情页面的webview:',driver.current_context)
        time.sleep(1)
        # 点击受理【详情页面是名字为'WEBVIEW_xweb'的webview中】
        driver.switch_to.context('WEBVIEW_xweb')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[6]/a[2]').click()
        time.sleep(1)
        # 点击取消按钮并点击输入框
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[6]/a[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='am-textarea-control']/textarea").click()
        time.sleep(1)
        #print(driver.contexts)
        driver.find_element_by_xpath("//div[@class='am-textarea-control']/textarea").send_keys(u"客人不需要了")
        time.sleep(1)
        driver.find_element_by_xpath(
            "//div[@class='am-modal-body']/div[@class='JW_C_modal-footer']/div[@class='JW_C_modal-footer-item primary']").click()
        # 点击链接进入微信公众号之后，需要切换上下文（webview），如果不能理解，则可以把他看成Iframe
        #time.sleep(1)
        WebDriverWait(driver, 2).until(
            lambda driver: driver.find_element_by_class_name('am-toast-text-info'))
        a = driver.find_element_by_class_name('am-toast-text-info').text
        #if (a == '取消成功'):
            #print('成功')
        self.assertEqual(a, '取消成功')
        driver.back()

    def tearDown(self):
        driver=self.driver

if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()
    #将测试用例，加入到测试容器中
    test.addTest(Open("test_menu"))
    test.addTest(Open("test_createwu"))
    test.addTest(Open("test_createsao"))
    test.addTest(Open("test_page"))
    test.addTest(Open("test_acceptaccept"))
    test.addTest(Open("test_acceptcancel"))

    #  设置报告文件保存路径

    report_path =  'D:\\AImanager\\wechat\\Result\\'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #  设置报告名称格式
    HtmlFile = report_path + now + "公众号.html"
    #print(HtmlFile)
    #  python3.0不支持file函数，可以用open()来替代
    file_result = open(HtmlFile,"wb")

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"公众号测试", description = u"用例执行情况")
    #运行测试用例
    runner.run(test)
    file_result.close()

