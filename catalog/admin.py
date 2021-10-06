from django.contrib import admin

from catalog.models import CodeType, Code


class CodeTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class CodeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'code_type',
        'metadata'
    ]


admin.site.register(CodeType, CodeTypeAdmin)
admin.site.register(Code, CodeAdmin)
