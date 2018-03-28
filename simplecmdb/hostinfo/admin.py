from django.contrib import admin

# Register your models here.
from hostinfo.models import Host
class HostAdmin(admin.ModelAdmin):
    list_display = [
                      "hostname",
                      "ip",
                      "cpu_model",
                      "cpu_num",
                      "memory",
                      "vendor",
                      "product",
                      "osver",
                      "sn"
                          ]
admin.site.register(Host,HostAdmin)



from hostinfo.models import HostGroup

class HostGroupAdmin(admin.ModelAdmin):
    list_display = ["groupname"]

admin.site.register(HostGroup, HostGroupAdmin)

