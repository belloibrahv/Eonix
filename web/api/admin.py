from django.contrib import admin

from .models import User, Career, Course, Topic

admin.site.register(User)
admin.site.register(Career)
admin.site.register(Course)
admin.site.register(Topic)
