__author__ = 'min.sun'
#断言那里需要将断言失败后，断言数量自增和存储断言具体情况的放到一个方法里去写更方便一些，下周来做
def report(result,assertresultlist):
    with open(r"C:\Users\min.sun\Desktop\自动化测试\report.txt",'a') as f:
        passnum="通过的测试模块数量："+(str(result[0]))+"\n"
        failurenum="失败的测试模块数量："+(str(result[1]))+"\n"
        assertfailurenum="失败的断言数量："+(str(result[2]))+"\n"
        f.write(passnum)
        f.write(failurenum)
        f.write(assertfailurenum)
        if(result[2]!=0):
            f.write("\n断言结果如下：\n\n\n")
            for assertresult in assertresultlist:
                a="{0: ^12}|{1: ^12}|{2: ^12}\n".format(assertresult["position"],assertresult["expect"],assertresult["now"])
                f.write(a)
        else:
            f.write("\n恭喜你，断言全部通过！\n")
list=[]
list.append(dict([("position","位置"),("expect","期望"),("now","首页-title")]))
list.append(dict([("position","1"),("expect","2"),("now","3")]))
#list = [{"position":"位置","expect":"期望","now":"实际"},{"position":"首页-title","expect":"孙一","now":"孙二"}]
#report([1,2,1],list)