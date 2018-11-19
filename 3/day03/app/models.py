from django.db import models

# Create your models here.
# 定义自己的model类
# 表名默认是: 应用名_类名
from django.utils import timezone


class User(models.Model):
    # 字段名命名规则：
    # 1 不能是python关键字
    # 2 不允许使用连续的下划线

    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=32)
    ip = models.CharField(max_length=15,null=True)
    allowed = models.BooleanField(default=True)

    # 查看对象具体信息，需要重写魔术方法__str__
    def __str__(self):
        return '用户名：' + self.username + " 密码： " + self.password

    # 添加删除方法不需要迁移
    def test(self):
        pass

    # 元信息
    class Meta:
        db_table = 'user'  #表名
