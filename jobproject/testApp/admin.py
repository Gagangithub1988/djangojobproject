from django.contrib import admin
from testApp.models import chennaijobs,hydjobs,mumbaijobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class mumbaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(mumbaijobs,mumbaijobsAdmin)
