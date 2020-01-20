from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    '''创建用户
    '''

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64, unique=True)
    is_admin = models.BooleanField(default=False)   # 管理员拥有所有权限
    is_staff = models.BooleanField(default=False)   # 协管员拥有部分管理权限
    is_active = models.BooleanField(default=True)   # 活动用户，被封时为 False

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_userid(self):
        return User.objects.get(username=self.username).user_id
