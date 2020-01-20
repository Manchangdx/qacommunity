from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    '''用户管理类，用于创建普通用户和超级用户
    '''

    def create_user(self, username, email, password, **kw):
        '''创建普通用户
        '''
        if not email:
            raise ValueError('Users must have avalid email address.')
        user = self.mode(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **kw):
        '''创建超级用户
        '''
        user = self.create_user(username, email, password, **kw)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
