from django.contrib import admin
from .models import CheckList,CheckListItem
# Register your models here.

class CheckListAdmin(admin.ModelAdmin):
    list_display=['title','is_deleted','is_archived','created_on','update_on']
admin.site.register(CheckList,CheckListAdmin)


class CheckListItemAdmin(admin.ModelAdmin):
    list_display=['text','is_checked','created_on','update_on','checklist']
admin.site.register(CheckListItem,CheckListItemAdmin)