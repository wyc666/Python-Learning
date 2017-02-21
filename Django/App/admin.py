# -*- coding: utf-8 -*-
from django.contrib import admin
from App import models

class AdminBBS(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'signature', 'view_count', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('title', 'auth__user__name')
    # list_editable = ('content',)

    # 定制签名显示在Admin中
    def signature(self, obj):
        return obj.author.signature

    signature.short_description = 'User Signature'

# Register your models here.
admin.site.register(models.BBS, AdminBBS)
admin.site.register(models.User)
admin.site.register(models.Category)
