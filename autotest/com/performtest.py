__author__ = 'min.sun'
import time
from com import getexcel
from com import operation
def perform(testsuit,filename,driver):
            testcaselist = getexcel.testcase(filename,testsuit["suitname"])
            if testcaselist is not None:
                print("正在执行套件",testsuit["suitname"])
                for testcase in testcaselist:
                    print(testcase)
                    operation.opration(testcase,driver)
                time.sleep(5)