# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect
from models import Host,Project,Service
from remote_ssh import SshConn
import os
shell_env="/bin/bash"

def index(request):
    obj = Host.objects.all().values("project__project_name")
    return  render(request,'start_opt/index.html',locals())

def service(request,project_name):
    if request.method == "POST":
        service_name = request.POST.get("service_name",None)
        ip_pj = Project.objects.filter(project_name=project_name).values("host__host_ip","project_dir")[0]
        remote_ip = ip_pj["host__host_ip"]
        pj_dir = ip_pj["project_dir"]
        shell_name = Service.objects.filter(service_name=service_name).values("restart_file")[0]["restart_file"]
        exec_comm = shell_env+" "+pj_dir+shell_name
        print exec_comm
        exec_comm = "/bin/bash /tmp/ceshi.sh"
        sshConn = SshConn()
        result = sshConn.exec_command(exec_comm)
        print result
        sshConn.sshclose()
        if not result:
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        project_name = project_name
        obj = Project.objects.filter(project_name=project_name).values("service__service_name","service__id")
        return render(request,'start_opt/service_list.html',locals())
