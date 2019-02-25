from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=11)
    email = models.EmailField()
    tel = models.CharField(max_length=11, validators=[RegexValidator(regex="^(136|176|184)\d{8}$", message="手机号不符合规范")])
    # 上传图片   路径
    img = models.ImageField(upload_to='user_image')
    # 类型
    c = models.IntegerField(choices=((0,"普通用户"),(1,"高级用户")),default=0)
    sh = models.IntegerField(verbose_name="申请状态", choices=((0,"未审核"),(1,"审核中"),(2,"审核通过")),default=0)

    # 粉丝
    flower = models.TextField(max_length=65535,default='')
    # 关注
    star = models.TextField(max_length=65535,default='')
    def __str__(self):
        return self.username
