__author__ = 'min.sun'
import time
from com import getexcel
from com import operation
def perform(testsuit,filename,driver,logger,result,assertresultlist):
            testcaselist = getexcel.testcase(filename,testsuit["suitname"])
            if testcaselist is not None:
                print("正在执行套件",testsuit["suitname"])
                #logger.info(u"正在执行套件",testsuit["suitname"])
                logger.info("测试套件【 %s 】正在执行..................",testsuit["suitname"])
                try:
                    for testcase in testcaselist:
                        print(testcase)
                        operation.opration(testcase,driver,logger,result,assertresultlist)
                    time.sleep(5)
                except Exception as e:
                    #执行套件内所有的测试用例，如果没有异常，增加失败数量
                    logger.error(e)
                    result[1] = result[1]+1
                    logger.info("失败数量加1")
                else:
                    #执行套件内所有的测试用例，如果没有异常，增加成功数量
                    logger.info("测试套件【 %s 】执行通过..................",testsuit["suitname"])
                    result[0] = result[0]+1
                    logger.info("通过数量加1")
            else:
                logger.warn("没有找到该测试套件 :%s",testsuit["suitname"])