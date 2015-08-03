#coding:utf-8
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from bson import json_util as json
import pymongo
from projectmanageapp.models import project
from django.template import Template, Context, RequestContext


# Create your views here.
# def current_datetime(request):
#     current_date = datetime.datetime.now()
#     return render_to_response('current_datetime.html', locals())
def edit(request,param):
    post = project.objects(id=param)[0]
    # if request.method == 'POST':
    #     # update field values and save to mongo
    #     post.title = request.POST['title']
    #     post.last_update = datetime.datetime.now()
    #     post.content = request.POST['content']
    #     post.save()
    #     template = 'index.html'
    #     params = {'Posts': project.objects}

    # elif request.method == 'GET':
    #     template = 'edit.html'
    #     params = {'post':post}
    return render_to_response("edit.html", locals(),context_instance=RequestContext(request))

def index(request):
    #使用models.py
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
    if request.method == 'POST' and request.POST['name'] is not None:
       name = request.POST['name']
       description = request.POST['description']
       pmember = request.POST['pmember']
       devmember = request.POST['devmember']
       testmember = request.POST['testmember']
       uimember = request.POST['uimember']
       post = project(name=name, pmember=pmember,devmember=devmember,testmember=testmember,uimember=uimember,status="测试中")
       post.last_update = datetime.now()
       post.save()

    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def newproject(request):
    # id = eval("request." + request.method + "['id']")
    # post = project.objects(id=id)[0]
    # if request.method == 'POST':
    #    name = request.POST['name']
    #    description = request.POST['description']
    #    pmember = request.POST['pmember']
    #    devmember = request.POST['devmember']
    #    testmember = request.POST['testmember']
    #    uimember = request.POST['uimember']
    #    post = project(name=name, pmember=pmember,devmember=devmember,testmember=testmember,uimember=uimember,status="测试中")
    #    post.last_update = datetime.now()
    #    post.save()
    return render_to_response('newproject.html', locals(),context_instance=RequestContext(request))

