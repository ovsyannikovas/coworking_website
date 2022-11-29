from django.contrib import admin

from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class EventListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'unique_num')
    readonly_fields = ('unique_num',)
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(EventList, EventListAdmin)
