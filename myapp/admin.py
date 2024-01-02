from django.contrib import admin
from .models import *


# # Register your models here.

admin.site.register(admission)
admin.site.register(contact_us)
admin.site.register(feedback)
admin.site.register(CommonFees)
admin.site.register(fees)
admin.site.register(playg)
admin.site.register(course_g)

class timetableAdmin(admin.ModelAdmin):
    list_display=['group_name','days','timing','content']
    list_filter=['group_name','days','timing']
    list_editable=['days','timing','content']

admin.site.register(timetable,timetableAdmin)
admin.site.register(time_slot)






class imgAdmin(admin.ModelAdmin):

    list_display=['student_images']
admin.site.register(img,imgAdmin)








# class admissionAdmin(admin.ModelAdmin):
#     list_display=['image','admission_for','student_id','student_name','age','date_of_birth','father_name','father_age','father_Contact_no','father_qualification','father_occupation','mother_name','mother_age','mother_Contact_no','mother_qualification','mother_occupation','email','address','caste_category']

# admin.site.register(admission,admissionAdmin) 





# class feedbackAdmin(admin.ModelAdmin):
#     list_display=['full_name','review','remark','Contact_no','suggestion']

# admin.site.register(feedback,feedbackAdmin)





# class contact_usAdmin(admin.ModelAdmin):
#     list_display=['contact_id','First_name','last_name','email','Contact_no','your_message']

# admin.site.register(contact_us,contact_usAdmin)
