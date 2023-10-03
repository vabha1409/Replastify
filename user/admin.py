from django.contrib import admin
from .models import Service
from .models import Contact,Collect,Subscribed


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")


admin.site.register(Contact, ContactAdmin)



class ServiceAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "industry", "bn", "wu", "jt", "years", "email", "number", "howhelp")


admin.site.register(Service, ServiceAdmin)


class CollectAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile", "location", "business", "feedback")


admin.site.register(Collect, CollectAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("name","email")


admin.site.register(Subscribed , SubscribeAdmin)

