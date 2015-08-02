#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from bson import json_util as json
import pymongo


# Create your views here.
# def current_datetime(request):
#     current_date = datetime.datetime.now()
#     return render_to_response('current_datetime.html', locals())
from django.template import Template, Context

def insert(request):
    id = eval("request." + request.method + "['id']")
    post ={}
    if request.method == 'POST':
        post.projectid = request.POST['projectid']
        print(post.projectid)
    else:

     return

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    #使用数据库
    client = pymongo.MongoClient("localhost",27017)
    db = client.projectmanager
    projectlist = db.project.find()
    STATIC_URI="C:/Users/msun.sun/Desktop/projectmanage/projectmanageapp/static/"

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
    return render_to_response('index.html', locals())

def newproject(request):
    return render_to_response('newproject.html', locals())
    return

def test(request):
    fp = open(r'C://Users/msun.sun/Desktop/projectmanage/projectmanageapp/templates/index.html',encoding= 'utf-8')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context())
    return HttpResponse(html)