from django.contrib import admin

from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Articles, ArticlesAdmin)


