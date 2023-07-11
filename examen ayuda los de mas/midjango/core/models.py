from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



# 登录信息模型
class LoginInfo(models.Model):
    username = models.CharField(max_length=255)  # 用户名
    password = models.CharField(max_length=255)  # 密码

# 用户模型
class User(models.Model):
    username = models.CharField(max_length=100)  # 用户名
    password = models.CharField(max_length=100)  # 密码
    # 添加其他字段以保存更多用户信息

    def __str__(self):
        return self.username

# 购买模型
class Purchase(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    @classmethod
    def create_from_item(cls, item):
        return cls(
            product_id=item['product_id'],
            name=item['name'],
            quantity=item['quantity'],
            amount=item['price']
        )

