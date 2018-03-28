from django.shortcuts import render

# Create your views here.
from hostinfo.models import Host,HostGroup
from django.http import HttpResponse
import pickle
import json

def getjson(req):
    ret_list = []
    hg = HostGroup.objects.all()
    for g in hg:
        ret = {"groupname":g.groupname,"members":[]}
        for h in g.members.all():
            ret_h = {"hostname":h.hostname,"ip":h.ip}
            ret["members"].append(ret_h)
        ret_list.append(ret)
    return HttpResponse(json.dumps(ret_list))


def gettxt(req):
    res = ""
    hg = HostGroup.objects.all()
    for g in hg:
        groupname = g.groupname
        for h in g.members.all():
            hostname = h.hostname
            ip = h.ip
            res += groupname +" " +hostname +" " +ip +"\n"
    return HttpResponse(res)


def collect(req):
    #print req
    if req.POST:
    #if req.method == "POST":
        #print req.body
        #print pickle.loads(req.body)
        #hostname = req.POST.get("hostname")
        #ip = req.POST.get("ip")
        #osver = req.POST.get("osver")
        #vendor = req.POST.get("vendor")
        #product = req.POST.get("product")
        #cpu_model = req.POST.get("cpu_model")
        #cpu_num = req.POST.get("cpu_num")
        #memory = req.POST.get("memory")
        #sn = req.POST.get("sn")
        
        #obj = pickle.loads(req.body)
        obj = json.loads(req.body)
        hostname = obj["hostname"]
        ip = obj["ip"]
        osver = obj["osver"]
        vendor = obj["vendor"]
        product = obj["product"]
        cpu_model = obj["cpu_model"]
        cpu_num = obj["cpu_num"]
        memory = obj["memory"]
        
        sn = obj["sn"]
        try:
            host = Host.objects.get(hostname=hostname)
        except:
            host = Host()

        host.hostname = hostname
        host.ip =ip      
        host.osver = osver
        host.product = product 
        host.cpu_model = cpu_model
        host.cpu_num = cpu_num
        host.memory = memory
        host.vendor = vendor
        host.sn = sn

        host.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("no data")  
