from django.contrib import admin

from .models import *


class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'user',)
    readonly_fields = ('unique_num',)
    search_fields = ('date_time', 'user',)



admin.site.register(Coworking, CoworkingAdmin)
