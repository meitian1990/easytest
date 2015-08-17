from django.db import models
# Create your models here.
from projectmanage.settings import DBNAME
from mongoengine import *
connect(DBNAME)

class project(Document):
    name = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=False)
    pmember = StringField(max_length=120, required=False)
    devmember = StringField(max_length=120, required=False)
    testmember = StringField(max_length=120, required=False)
    uimember = StringField(max_length=120, required=False)
    status = StringField(max_length=120, required=False)
    date = DateTimeField(required=False)
    last_update = DateTimeField(required=False)
    title = StringField(max_length=120)
    file = FileField()
# class UploadFile(Document):
#     project = models.ForeignKey(project)
#     title = StringField(max_length=120)
#     file = FileField()
# for e in project.objects.all():
#     print(e["id"], e["name"], e["pmember"])