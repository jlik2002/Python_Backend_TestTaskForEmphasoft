
from __future__ import unicode_literals
from django.db import models
from django.db import transaction
from django.utils import timezone, translation
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self,email,login,password,**extra_kwargs ):
        if not email:
            raise ValueError('Need email')
        if not login:
            raise ValueError('Need login')
        if not password:
            raise ValueError('Need password')
        try:
            with transaction.atomic():
                user = self.model(email=email,login=login,**extra_kwargs)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
    def create_user(self,email,login,**extra_kwargs):
        return self._create_user(email,login,**extra_kwargs)
    


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    login = models.CharField(max_length=30,unique=True)
    firstname = models.CharField(max_length=80,blank=True) 
    lastname = models.CharField(max_length=80,blank=True) 
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()
    USERNAME_FIELD = 'login'
    EMAIL_FIELD = ' email'
    REQUIRED_FIELDS = ['firstname','lastname'] 
    def save(self, *args,**kwargs):
        super(User,self).save(*args,**kwargs)
        return self
