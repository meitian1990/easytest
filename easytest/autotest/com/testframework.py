__author__ = 'min.sun'
#coding:utf-8
from selenium import webdriver
import unittest
from com import getexcel
from com import performtest
from com import report
from com import operation
import time
import logging
import logging.config

#增加日志，通过配置文件来增加log
logging.config.fileConfig(r"C:\Users\min.sun\Desktop\autotest\com\log.conf", disable_existing_loggers=False)
logger = logging.getLogger("performtest")
#获得测试套件内容
testsuitfilename = "C:/Users/min.sun/Desktop/自动化测试/testcase.xlsx"
testsuitlist = getexcel.getsuit(testsuitfilename,logger)

class testcase(unittest.TestCase):
    def setUp(self):
        print("it is setup")
        logger.info("测试开始......................")
        self.profileDir = "C:/Users/min.sun/AppData/Roaming/Mozilla/Firefox/Profiles/cyy0p6gm.default"
        self.profile = webdriver.FirefoxProfile(self.profileDir)
        self.driver = webdriver.Firefox(self.profile)
        self.driver.maximize_window()
        #报告结果统计到一个列表result中，result[0]表示pass的suit，result[1]表示failure的suit，result[2]表示断言失败的数量
        self.result = [0,0,0]
        self.assertresultlist = []
        # self.testsuitlist = getexcel.getsuit(testsuitfilename)
    #调用执行的方法，遍历套件进行执行，但是测试会显示只有一条，这个不好，需要更改，或者自己存储日志，打印报告。
    def test(self):
        for testsuit in testsuitlist:
            a = "test_"+testsuit["suitmethodname"]
            performtest.perform(testsuit,testsuitfilename,self.driver,logger,self.result,self.assertresultlist)
            self.driver.implicitly_wait(10)
    #执行测试用例，登录测试用例，已经测试通过，是ok的
    # def test(self):
    #     testcaselist = getexcel.testcase(testsuitfilename,"登录用例")
    #     for testcase in testcaselist:
    #         print(testcase)
    #         operation.opration(testcase,self.driver)
    #     time.sleep(5)





    # 在遍历套件的时候遇到了问题，想将套件的名字当做变量加到def中，但是一直都提示是非法的，这个以后再解决
    # def "test_"+suit["suitmethodname"](self):
    #     print("it is run")

    # #循环遍历测试套件，寻找里面执行为YES的测试套件，去执行相应的测试用例
    # for testsuit in testsuits:
    #     #XXX为要执行的测试用例模块的名字，例如登录用例
    #     def XXXX(self):
    #         #YYY为相应的用例模块的用例sheet，取出该用例后循环遍历去执行方法
    #         for testcase in testsuit:
    #             #执行的具体用例，点击元素等，（这里可以写一个单独的方法）

    def tearDown(self):
        print("it is over")
        logger.info("测试结束………………………………………………")
        self.driver.quit()
        logger.info("测试结束,等待打印报告………………………………………………")
        report.report(self.result,self.assertresultlist)
        logger.info("报告打印完毕………………………………………………")
if __name__=="__main__":
    unittest.main


