#coding:utf-8
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from bson import json_util as json
import pymongo
from projectmanageapp.models import project
from django.template import Template, Context, RequestContext
from mongoengine import *



# Create your views here.
# def current_datetime(request):
#     current_date = datetime.datetime.now()
#     return render_to_response('current_datetime.html', locals())
def uploadfile(request):
    # if request.method == "POST":
    #     form = UploadFile(request.POST,request.FILES)
    #     if form.is_valid():
    #         # handle_uploaded_file(request.FILES['file'])
    #         return
    return

def delete(request):
    if request.method=="POST":
        id = request.POST["del"]
        post = project.objects(pk=id)[0]
        post.delete()
    return HttpResponseRedirect("/index/")
def edit(request,param):
    #IBM方法中的
    # post = project.objects(id=param)[0]
    #小稳子建议用pk替换id，pk主键的意思，据说更规范一些
    # post = project.objects(pk=param)[0]
    #小稳子建议用get
    post = project.objects.get(pk=param)
    for i in project.objects(pk=param):
        print(i)
    if request.method == 'POST':
        # update field values and save to mongo
        id = param
        name = request.POST['name']
        description = request.POST['description']
        pmember = request.POST['pmember']
        devmember = request.POST['devmember']
        testmember = request.POST['testmember']
        uimember = request.POST['uimember']
        post = project(id=param,name=name, description=description,pmember=pmember,devmember=devmember,testmember=testmember,uimember=uimember,status="测试中")
        post.last_update = datetime.now()
        post.save()
        # return index(request)
        return HttpResponseRedirect('/index/')

    # elif request.method == 'GET':
    #     templatep = 'edit.html'
    #     post = project.objects(id=param)[0]
    return render_to_response("edit.html", locals(),context_instance=RequestContext(request))
def index(request,content=""):
    #使用models.py
    if content:
        projectlist = project.objects(name=content)
    else:
        projectlist = project.objects
    #使用数据库
    # client = pymongo.MongoClient("localhost",27017)
    # db = client.projectmanager
    # projectlist = db.project.find()
    #使用循环，给予一个列表
    # projectlist=[{"name":"聊聊大人","pmember":"华华1","devmember":"兽兽1","testmember":"炫炫1","uimember":"雨欣1","date":"2015-8-1","status":"整装待发"},
    # {"name":"聊聊大人","pmember":"华华2","devmember":"兽兽2","testmember":"炫炫2","uimember":"雨欣2","date":"2015-8-1","status":"整装待发"},
    # ]

    #使用单条数据
    # name="聊聊大人"
    # pmember="华华2"
    # devmember="兽兽2"
    # testmember="炫炫2"
    # uimember="雨欣2"
    # date="2015-8-1"
    # status="整装待发"

    #暂时隐藏的保存操作

    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def newproject(request):
    if request.method == 'POST' and request.POST['name'] is not None:
        name = request.POST['name']
        description = request.POST['description']
        pmember = request.POST['pmember']
        devmember = request.POST['devmember']
        testmember = request.POST['testmember']
        uimember = request.POST['uimember']
        post = project(name=name, description=description,pmember=pmember,devmember=devmember,testmember=testmember,uimember=uimember,status="测试中")
        profile = request.FILES["proupload"]
        post.file.put(profile)
        # post.file.put(open(r'C:\\Users\min.sun\Desktop\阿布.jpg','rb'))
        post.last_update = datetime.now()
        post.save()
        return HttpResponseRedirect('/index/')

    return render_to_response('newproject.html', locals(),context_instance=RequestContext(request))

