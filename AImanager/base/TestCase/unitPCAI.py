import unittest
import HTMLTestRunner
import time
from selenium.webdriver.support.ui import WebDriverWait
from AImanager.base.TestCase.user_login import *
from AImanager.base.TestCase.注册服务员报告 import *

if __name__ == "__main__":
    #定义一个容器
    suite = unittest.TestSuite()
    # 将测试用例，加入到测试容器中
    suite.addTest(Login("test_login"))
    """
    test.addTest(Waiter("test_waiter"))
    test.addTest(Service("test_invoice"))
    test.addTest(Service("test_bed"))
    test.addTest(Service("test_morning_call"))
    test.addTest(Monitor("test_create_bed"))
    test.addTest(Monitor("test_create_morningcall"))
    test.addTest(Monitor("test_create_clean"))
    test.addTest(Monitor("test_create_laundry"))
    test.addTest(Monitor("test_create_fix"))
    """
    # 设置报告文件保存路径
    #report_path = '/Users/mtt/PycharmProjects/AImanager/base/Result'
    report_path = '../Result'
    #  获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(now)
    #  设置报告名称格式
    HtmlFile = os.path.join(report_path, "AI管家.html")
    #HtmlFile = report_path + now + "AI管家.html"
    #  python3.0不支持file函数，可以用open()来替代
    file_result = open(HtmlFile, "wb")
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"AI管家自动化测试", description=u"用例执行情况")
    # 运行测试用例
    runner.run(suite)
    file_result.close()
