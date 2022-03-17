from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy

# Create your models here.

class Create_Admin(BaseUserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please Enter your Email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Admin have to be must is_staff = True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Admin have to be must is_superuser = True")
        
        if extra_fields.get('is_active') is not True:
            raise ValueError("Admin have to be must is_active = True")
        
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email =models.EmailField(unique=True, null=False, max_length=254)
    is_staff = models.BooleanField(gettext_lazy('Staff Status'), default=False, help_text=gettext_lazy('Is only for admin'))
    is_active = models.BooleanField(gettext_lazy('Active'), default=False, help_text=gettext_lazy('Is only for admin'))
    USERNAME_FIELD='email'
    objects= Create_Admin()
    
    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
