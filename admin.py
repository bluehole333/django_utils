import traceback

from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from base.admin import *
from core.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
# from related_admin import RelatedFieldAdmin, getter_for_related_field
from base.config import *


@admin.register(ModelName)
class IntervieweeAdmin(admin.ModelAdmin):
    # 列表显示的字段
    list_display = ['title', 'timestamp', 'author']
    # 可以查询的字段，显示搜索框
    search_fields = ['title']
    # 可以修改内容的链接
    list_display_links = ['author']
    # 可直接编辑的字段（但是不能同时可连接可编发来）
    list_editable = ['title']
    # 定制过滤器
    list_filter = ['author']
    # 只读字段
    readonly_fields = ("RefCount", )

    # 自定义模板
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None

    def show_name(self, obj):
        if obj.ref_id:
            return Interviewee.objects.get(pk=obj.ref_id).nick_name

        return '-'

    show_name.short_description = '列显示文案'
