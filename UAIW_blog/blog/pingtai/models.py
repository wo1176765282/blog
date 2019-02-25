from django.db import models
from django.utils.html import format_html
from django.utils.safestring import SafeText
from django.contrib.auth.models import User as django_user
from ckeditor.fields import RichTextField

# Create your models here.
# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="分类")
    def listKeyword(self):
        objs = self.keyword_set.all()
        arr = []
        for item in objs:
            arr.append("<span style='margin:0 5px'>"+item.name+"</span>")
        # print(SafeText("".join(arr)))
        return SafeText("".join(arr))
    def __str__(self):
        return self.name
    # 修改行内的表头
    listKeyword.short_description="关键字"
    class Meta:
        verbose_name = "分类管理"
        # verbose_name_plural = "分类管理"
    # 类方法
    @classmethod
    def getAll(cls):
        return cls.objects.all()

class Keyword(models.Model):
    name = models.CharField(max_length=20,verbose_name="关键字")
    c = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# 平台文章
class PTArticle(models.Model):
    c = models.ForeignKey(verbose_name="分类", to=Category, on_delete=models.CASCADE)
    k = models.ForeignKey(verbose_name="关键字", to=Keyword, on_delete=models.CASCADE)
    a = models.ForeignKey(verbose_name="作者",to=django_user, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="文章标题", max_length=50)
    con = RichTextField(verbose_name="文章内容", max_length=20000)
    c_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    u_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    look = models.IntegerField(verbose_name="浏览量", default=0)
    @classmethod
    def getAll(cls):
        return cls.objects.all()
    class Meta:
        verbose_name = "添加文章"
        # verbose_name__plural = '添加文章'

from userauth.models import User
class UserInfo(models.Model):
    u = models.OneToOneField(to=User,on_delete=models.CASCADE)
    company = models.CharField(max_length=30, verbose_name='公司')
    # 职位
    position = models.CharField(max_length=30, verbose_name='职位')
    hobby = models.CharField(max_length=100, verbose_name='爱好')
    reason = models.TextField(max_length=300, verbose_name='原因')
    realname = models.CharField(max_length=20, verbose_name='姓名')
    s_time = models.DateTimeField(verbose_name="申请时间", auto_now_add=True)
    p_time = models.DateTimeField(verbose_name="通过时间", auto_now=True)

    def sh_status(self):
        num = self.u.sh
        status = ''
        color = ''
        if num==0:
            color = 'black'
            status = '未审核'
        elif num ==1:
            color = 'red'
            status = '待审核'
        else:
            color = 'green'
            status = '审核通过'
        return SafeText('<span style="color:'+color+';">'+status+'</span>')

    class Meta:
        verbose_name = "博客审核"
        verbose_name_plural = '博客审核'

    sh_status.short_description = '审核状态'

