__author__ = 'min.sun'
#定位元素
def by_id(testcase,driver):
    return driver.find_element_by_id(testcase["testelement"])
def by_class_name(testcase,driver):
    return driver.find_element_by_class_name(testcase["testelement"])
def by_css_selector(testcase,driver):
    return driver.find_element_by_css_selector(testcase["testelement"])
def by_xpath(testcase,driver):
    return driver.find_element_by_xpath(testcase["testelement"])

def findelement(testcase,driver):
    findelements = dict(by_id=by_id,by_class_name=by_class_name,by_css_selector=by_css_selector,by_xpath=by_xpath)
    return findelements[testcase["positionway"]](testcase,driver)