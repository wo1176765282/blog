from django.contrib import admin
from .models import Category,Keyword,PTArticle,UserInfo
from django.contrib.admin import AdminSite
from django.contrib.admin.models import ADDITION, LogEntry
from userauth.models import User

# Register your models here.
AdminSite.site_header="天涯博客后台站点"


class KeywordInline(admin.StackedInline):
    model = Keyword
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name','listKeyword']
    inlines = [KeywordInline]

@admin.register(PTArticle)
class PTArticleAdmin(admin.ModelAdmin):
    # exclude = []
    list_display = ['title', 'c', 'k', 'a', 'c_time', 'u_time']
    # 更换跳转的页面。
    # add_form_template = "admin/addPTArticle.html"
    class Media:
        js = ('pingtai/js/addPTArticle.js',)
    readonly_fields = ['a']
    # 分页
    list_per_page=5
    # 搜索的字段  只能定义一个  是外键的不可以直接搜索
    search_fields = ['title']
    # 过滤器
    list_filter = ['a','c','k']
    # 更改列表页面将包含该字段的基于日期的向下钻取导航  通过日期查询
    date_hierarchy='u_time'
    # 添加时执行的方法
    def add_view(self, request, form_url='', extra_context=None):
        print("正在打开add_view")
        return super().add_view(request,form_url, extra_context)

    def save_model(self, request, obj, form, change):
        obj.a = request.user
        return super().save_model(request,obj,form,change)

    def fabu(self,request,queryset):
        queryset.update(status=False)

    def chehui(self,request,queryset):
        queryset.update(status=False)

    chehui.short_description = "撤回发布"
    fabu.short_description = "发布"

    actions = [chehui, fabu]

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # exclude = []
    fields = ['u', 'realname', 'company', 'position', 'hobby', 'reason', 's_time','sh_status']
    readonly_fields = ['u', 'realname', 'company', 'position', 'hobby', 'reason', 's_time','sh_status']
    list_display = ['realname', 'company', 'position', 'hobby', 'reason', 's_time','sh_status']

    def ok(self,request,queryset):
        for item in queryset.all():
            User.objects.filter(id=item.u_id).update(sh=2)

    def no(self, request, queryset):
        for i in queryset.all():
            User.objects.filter(id=i.u_id).update(sh=1)

    ok.short_description = '审核通过'
    no.short_description = '驳回审核'
    actions = [ok, no]
    # search_fields = ['s_time', 'company', 'position']  # 搜索字段
    list_per_page = 10  # 每页显示的数据（分页）
    # list_filter = ['sh_status']
