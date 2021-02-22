from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'date')


class CategoryComment(admin.ModelAdmin):
    list_display = ("id", 'author', 'date', "comment")


admin.site.register(Project, CategoryAdmin)
admin.site.register(Comment, CategoryComment)
admin.site.register(Contacts, CategoryAdmin)
admin.site.register(Progress)
