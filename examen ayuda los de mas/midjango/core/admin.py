from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import LoginInfo

class LoginInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # 在 admin 后台中显示的字段列表
    search_fields = ('username', 'password')  # 在 admin 后台中可搜索的字段

admin.site.register(LoginInfo, LoginInfoAdmin)  # 将 LoginInfo 模型注册到 admin 后台

# 注销默认的 User 模型注册
admin.site.unregister(User)

# 创建一个新的 UserAdmin 类，继承自 BaseUserAdmin
class CustomUserAdmin(BaseUserAdmin):
    inlines = []  # 在编辑用户时显示的关联对象的列表

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

# 注册修改后的 User 模型并关联自定义的 Admin 配置类
@admin.register(User)
class CustomUserAdmin(CustomUserAdmin):
    groups = None  # 在 admin 后台中不显示用户所属的组
    user_permissions = None  # 在 admin 后台中不显示用户的权限

# 为自定义 User 模型的字段添加 related_name 参数
User.groups.field.related_name = 'custom_user_groups'  # 用户所属组的反向关联名
User.user_permissions.field.related_name = 'custom_user_permissions'  # 用户的权限的反向关联名
