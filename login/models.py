from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.


class CustomerUserManager(BaseUserManager):
    def create_user(self,email,username,password = None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email = email,username = username, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,username,password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length= 30, unique= True)
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    date_joined = models.DateField(null= True)
    phone_number = models.CharField(max_length= 20)
    account_number = models.CharField(max_length= 10, blank= True, null= True)
    balance = models.DecimalField(max_digits= 10, decimal_places= 2, default= 0.00)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= True)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'date_joined']

    def __str__(self):
        return self.email


