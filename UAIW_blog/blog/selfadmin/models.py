from django.db import models
from userauth.models import User
# Create your models here.
from pingtai.models import PTArticle,Category,Keyword
from userauth.models import User
from ckeditor.fields import RichTextField

class Artical(models.Model):
    a = models.ForeignKey(to=User, on_delete=models.CASCADE)
    c = models.ForeignKey(verbose_name="分类", to=Category, on_delete=models.CASCADE)
    k = models.ForeignKey(verbose_name="关键字", to=Keyword, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="文章标题", max_length=50)
    con = RichTextField(verbose_name="文章内容", max_length=20000)
    c_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    u_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    look = models.IntegerField(verbose_name="浏览量", default=0)
    status = models.BooleanField(default=False, verbose_name='发布状态')

