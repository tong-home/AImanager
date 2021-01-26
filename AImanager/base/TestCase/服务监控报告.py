#coding:utf-8
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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Monitor(unittest.TestCase):
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

    #手动新增加床客需
    def test_create_bed(self):
        driver = self.driver
        # 点击进入服务监控页面并新增
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@class="tab-container"]/button[@class="zent-btn-primary zent-btn"]').click()
        # 选择新增加床服务类型
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        driver.find_element_by_css_selector('span[value="15"]').click()
        # 选择楼层
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()
        #time.sleep(1)
        shi2 = time.strftime("%m/%d %H:%M", time.localtime(time.time()))
        time.sleep(1)
        # 获取toast内容
        a = driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text
        #print(u'获取的文字为：', a)
        self.assertEqual(a,'增加成功')

        #  设置报告文件保存路径
        png_path = 'D:\\AImanager\\base\\Image\\'
        #  获取系统当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #  设置报告名称格式
        Pngname = now + "创建加床"
        # 网页截图并保存
        driver.get_screenshot_as_file(png_path + Pngname + ".png")

        # 查询到加床服务是否是刚才新增的（根据服务类型和创建时间来判断）
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.find_element_by_css_selector('span[value="15"]').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(1)
        shi1 = driver.find_element_by_xpath(
            '// *[ @ id = "root"] / div[2] / div[2] / div[2] / div / div[3] / div[1] / div / div / table / tbody / tr[1] / td[6] / span').text
        self.assertEqual(shi1,shi2)
        time.sleep(1)


    def test_create_morningcall(self):
        driver = self.driver
        driver.refresh()
        time.sleep(1)
        # 点击进入服务监控页面并新增
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="tab-container"]/button[@class="zent-btn-primary zent-btn"]').click()

        # 选择叫醒服务类型
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        driver.find_element_by_css_selector('span[value="8"]').click()
        # 选择楼层
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        #time.sleep(2)
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
        # 选择叫醒服务的预约时间为2020-12-08
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/span[2]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/div[2]/div/ul[4]/li[3]/div').click()
        driver.find_element_by_css_selector('div.date-panel > div.date-table.panel-table > div > ul:nth-child(5) > li:nth-child(5) > div[title="2020-12-31"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()
        shi2 = time.strftime("%m/%d %H:%M", time.localtime(time.time()))
        time.sleep(1)
        # 获取toast内容
        a = driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text

        #  设置报告文件保存路径
        png_path = 'D:\\AImanager\\base\\Image\\'
        #  获取系统当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #  设置报告名称格式
        Pngname = now + "创建叫醒"
        # 网页截图并保存
        driver.get_screenshot_as_file(png_path + Pngname + ".png")

        # 查询到叫醒服务
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.find_element_by_css_selector('span[value="8"]').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(1)
        shi1 = driver.find_element_by_xpath('// *[ @ id = "root"] / div[2] / div[2] / div[2] / div / div[3] / div[1] / div / div / table / tbody / tr[1] / td[6] / span').text
        self.assertEqual(shi1,shi2)
        time.sleep(1)




    # 手动新增洗衣服务客需
    def test_create_laundry(self):
        driver = self.driver
        driver.refresh()
        time.sleep(1)
        # 点击进入服务监控页面并新增洗衣服务
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="tab-container"]/button[@class="zent-btn-primary zent-btn"]').click()
        # 选择新增打扫服务类型
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_css_selector('span[value="3"]').click()
        # 选择楼层
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()
        #time.sleep(1)
        shi2 = time.strftime("%m/%d %H:%M", time.localtime(time.time()))
        time.sleep(1)
        # 获取toast内容
        a = driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text
        # print(u'获取的文字为：', a)
        self.assertEqual(a, '增加成功')

        #  设置报告文件保存路径
        png_path = 'D:\\AImanager\\base\\Image\\'
        #  获取系统当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #  设置报告名称格式
        Pngname = now + "创建洗衣"
        # 网页截图并保存
        driver.get_screenshot_as_file(png_path + Pngname + ".png")

        # 查询到洗衣服务是否是刚才新增的（根据服务类型和创建时间来判断）
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.find_element_by_css_selector('span[value="3"]').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(1)
        shi1 = driver.find_element_by_xpath(
            '// *[ @ id = "root"] / div[2] / div[2] / div[2] / div / div[3] / div[1] / div / div / table / tbody / tr[1] / td[6] / span').text
        self.assertEqual(shi1,shi2)
        time.sleep(1)




    # 手动新增打扫服务客需
    def test_create_clean(self):
        driver = self.driver
        driver.refresh()
        time.sleep(1)
        # 点击进入服务监控页面并新增
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@class="tab-container"]/button[@class="zent-btn-primary zent-btn"]').click()
        # 选择新增打扫服务类型
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
        time.sleep(1)
        driver.find_element_by_css_selector('span[value="2"]').click()
        # 选择楼层
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()
        #time.sleep(1)
        shi2 = time.strftime("%m/%d %H:%M", time.localtime(time.time()))
        time.sleep(1)
        # 获取toast内容
        a = driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text
        # print(u'获取的文字为：', a)
        self.assertEqual(a, '增加成功')

        #  设置报告文件保存路径
        png_path = 'D:\\AImanager\\base\\Image\\'
        #  获取系统当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #  设置报告名称格式
        Pngname = now + "创建打扫"
        # 网页截图并保存
        driver.get_screenshot_as_file(png_path + Pngname + ".png")

        # 查询到加床服务是否是刚才新增的（根据服务类型和创建时间来判断）
        driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.find_element_by_css_selector('span[value="2"]').click()
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(1)
        shi1 = driver.find_element_by_xpath(
            '// *[ @ id = "root"] / div[2] / div[2] / div[2] / div / div[3] / div[1] / div / div / table / tbody / tr[1] / td[6] / span').text
        self.assertEqual(shi1, shi2)
        time.sleep(1)



        # 手动新增报修服务客需
    def test_create_fix(self):
            driver = self.driver
            driver.refresh()
            time.sleep(1)
            # 点击进入服务监控页面并新增
            driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '//*[@class="tab-container"]/button[@class="zent-btn-primary zent-btn"]').click()
            # 选择新增打扫服务类型
            driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div').click()
            driver.find_element_by_css_selector('span[value="14"]').click()
            # 选择楼层
            driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-1"]/div/div[1]/span').click()
            driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-2"]/div/div[1]/span').click()
            driver.find_element_by_xpath('//*[@id="zent-tabpanel-1-3"]/div/div[1]/span').click()
            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[1]').click()
            shi2 = time.strftime("%m/%d %H:%M", time.localtime(time.time()))
            time.sleep(1)
            # 获取toast内容
            a = driver.find_element_by_xpath('/html/body/div[2]/div/div/div').text
            # print(u'获取的文字为：', a)
            self.assertEqual(a, '增加成功')

            #  设置报告文件保存路径
            png_path = 'D:\\AImanager\\base\\Image\\'
            #  获取系统当前时间
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            #  设置报告名称格式
            Pngname = now + "创建报修"
            # 网页截图并保存
            driver.get_screenshot_as_file(png_path + Pngname + ".png")

            # 查询到加床服务是否是刚才新增的（根据服务类型和创建时间来判断）
            driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div').click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_css_selector('span[value="14"]').click()
            driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/button').click()
            time.sleep(1)
            shi1 = driver.find_element_by_xpath(
                '// *[ @ id = "root"] / div[2] / div[2] / div[2] / div / div[3] / div[1] / div / div / table / tbody / tr[1] / td[6] / span').text
            self.assertEqual(shi1, shi2)
            time.sleep(1)
            driver.quit()



    def tearDown(self):
        #self.driver.quit()
        driver=self.driver

'''
if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()

    #将测试用例，加入到测试容器中
    test.addTest(Monitor("test_create_bed"))
    test.addTest(Monitor("test_create_morningcall"))
    test.addTest(Monitor("test_create_clean"))
    test.addTest(Monitor("test_create_laundry"))
    test.addTest(Monitor("test_create_fix"))


    #  设置报告文件保存路径
    report_path =  'D:/AImanager/base/Result/'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #  设置报告名称格式
    HtmlFile = report_path + now + "服务监控.html"
    print(HtmlFile)
    #  python3.0不支持file函数，可以用open()来替代
    # file_result = file(HtmlFile, "wb")
    file_result = open(HtmlFile, "wb")  # 写入

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"AI管家服务监控页面测试", description = u"新增加床、报修、叫醒、洗衣、打扫的用例执行")

    #运行测试用例
    runner.run(test)
    file_result.close()
'''