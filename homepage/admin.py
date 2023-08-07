from django.contrib import admin
from . models import CustomUser,Events,Membership,Image, Feedback, Achievement
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Events)
admin.site.register(Membership)
admin.site.register(Image)
admin.site.register(Feedback)
admin.site.register(Achievement)


