from django.contrib import admin
from .models import News,Course ,Teacher , Blog
# Register your models here.

admin.site.register(News)

admin.site.register(Course)

admin.site.register(Teacher)

admin.site.register(Blog)
