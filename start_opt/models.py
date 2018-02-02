# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Host(models.Model):
    host_ip = models.GenericIPAddressField(verbose_name="IP地址")
    project = models.ManyToManyField("Project")
    create_date = models.DateField(auto_created=True)

    def __unicode__(self):
        return  self.host_ip

class Project(models.Model):
    project_name = models.CharField(max_length=32,verbose_name="项目名")
    create_date = models.DateField(auto_created=True)
    project_dir = models.CharField(max_length=64,verbose_name="项目目录")
    service = models.ManyToManyField("Service")

    def __unicode__(self):
        return self.project_name

class Service(models.Model):
    service_name = models.CharField(max_length=32,verbose_name="服务名")
    start_file = models.CharField(max_length=128,verbose_name="启动命令",null=True,blank=True)
    stop_file = models.CharField(max_length=128,verbose_name="停止命令",null=True,blank=True)
    restart_file = models.CharField(max_length=128,verbose_name="重启命令")
    create_date = models.DateField(auto_created=True)

    def __unicode__(self):
        return  self.service_name
