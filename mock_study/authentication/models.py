from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

"""
Extending from the base user class, we can create models for the nurse, research assistants, priniciple investigator, and statisticians.
"""

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        email_address = self.normalize_email(email)
        user = self.model(email=email_address, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active(True)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):

        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, default="John")
    last_name = models.CharField(max_length=50, default="Doe")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        return True
    
    def has_module_perms(self, app_label):

        return True

