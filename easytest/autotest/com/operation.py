__author__ = 'min.sun'
from com import find_element

#下一步需要将testcase["testoperation"]参数化，替换by_id
def click(testcase,driver):
    return find_element.findelement(testcase,driver).click()
    # if testcase["positionway"] == "by_id":
    #     return driver.find_element_by_id(testcase["testelement"]).click()
    # elif testcase["positionway"] == "by_class_name":
    #     return driver.find_element_by_class_name(testcase["testelement"]).click()
    # elif testcase["positionway"] == "by_css_selector":
    #     return driver.find_element_by_css_selector(testcase["testelement"]).click()
    # elif testcase["positionway"] == "by_xpath":
    #     return driver.find_element_by_xpath(testcase["testelement"]).click()
def send_keys(testcase,driver):
    return find_element.findelement(testcase,driver).send_keys(testcase["testdata"])
    # if testcase["positionway"] == "by_id":
    #     return driver.find_element_by_id(testcase["testelement"]).send_keys(testcase["testdata"])
    # elif testcase["positionway"] == "by_class_name":
    #     return driver.find_element_by_class_name(testcase["testelement"]).send_keys(testcase["testdata"])
    # elif testcase["positionway"] == "by_css_selector":
    #     return driver.find_element_by_css_selector(testcase["testelement"]).send_keys(testcase["testdata"])
    # elif testcase["positionway"] == "by_xpath":
    #     return driver.find_element_by_xpath(testcase["testelement"]).send_keys(testcase["testdata"])
def get(testcase,driver):
    return driver.get(testcase["testelement"])

#断言

#断言某元素的内容是否为期望的数据，例如判断首页的元素"showname"的值是不是孙一
def assertText(testcase,driver):
    try:
        # now = driver.find_element_by_id(testcase["testelement"]).get_attribute("innerHTML")
        now = find_element.findelement(testcase,driver).get_attribute("innerHTML")
        expect = testcase["testdata"]
        assert now == expect
    except AssertionError:
        print(testcase["testobject"],"实际上得到的不是我们想要的数据",expect,"而是",now)
        driver.save_screenshot(r"C:\Users\min.sun\Desktop\自动化测试\断言失败的页面截图\断言失败_"+testcase["pageobject"]+"_"+testcase["testobject"]+".png")
    return

#断言判断当前页面的title是不是与期望的数据一致
def assertTitle(testcase,driver):
    try:
        now = driver.title
        expect = testcase["testdata"]
        assert now == expect
    except AssertionError:
        print(testcase["testobject"],"不正确，不是",expect,"而是",now)
        driver.save_screenshot(r"C:\Users\min.sun\Desktop\自动化测试\断言失败的页面截图\断言失败_"+testcase["pageobject"]+"_"+testcase["testobject"]+".png")
    return

def opration(oper,driver):
    #对元素的常用操作，不包含复杂的操作，click(),get,send_keys等cxv x
    #暂时也将断言的写在这里，oper是方法里对应的testcase
    operator = dict(get=get,click=click,send_keys=send_keys,assertText=assertText,assertTitle=assertTitle)
    operator[oper["testoperation"]](oper,driver)



#
# test1 = {"testoperation":"get"}
# opration(test1,None)







# class operation(Webdriver):
#     def __init__(self,driver):
#         self.driver = driver
#         self.operator = {"get":get,"click":click,"send_keys":send_keys}
#     def click(self,testcase):
#         return self.driver.find_element_By_id(testcase["testelement"]).click()
#     def send_keys(self,testcase):
#         return self.driver.find_element_By_id(testcase["testelement"]).send_keys(testcase["testdata"])
#     def get(self,testcase):
#         return self.driver.get(testcase["testelement"])
#
#     def opration(self,oper):
#         self.operator[oper["testoperation"]](oper)