from django.contrib import admin
from .models import *

# Register your models here
class loginAdmin(admin.ModelAdmin):
    list_display=['name','password']

admin.site.register(login,loginAdmin)

class SurveyAdmin(admin.ModelAdmin):
    list_display=['text']
    
admin.site.register(Survey,SurveyAdmin)

class SignAdmin(admin.ModelAdmin):
    list_display=['username','email','password','cnfpass']
    
admin.site.register(Sign,SignAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display=['com_name','location','duration','services']
    
admin.site.register(Client,ClientAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=['enq_name','enq_email','enq_phone','enq_location','enq_service']
    
admin.site.register(Enquiry,EnquiryAdmin)