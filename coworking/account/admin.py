from django.contrib import admin

from .models import *



class CoworkingAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'user',)
    readonly_fields = ('unique_num',)
    search_fields = ('date_time', 'user',)



admin.site.register(Coworking, CoworkingAdmin)

class EventRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(EventOrgRequest, EventRequestAdmin)

