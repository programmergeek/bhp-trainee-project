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


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('nurse', 'Nurse'),
        ('research_assistant', 'Research Assistant'),
        ('principle_investigator', 'Principle Investigator'),
        ('statistician', 'Statistician')
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, default="John")
    last_name = models.CharField(max_length=50, default="Doe")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email.__str__()

    def has_perm(self, perm, obj=None):

        return True
    
    def has_module_perms(self, app_label):

        return True
    
    class Meta:
        permissions = [
            ('create_participant', "Create participant"),
            ('update_participant', "Update participant"),
            ('record_vitals', "Create new participant vitals record"),
            ('update_vitals', "Update participant vitals record"),
            ('view_vitals', "View participant vitals"),
            ('create_adverse_event', "Create adverse event report"),
            ('update_adverse_event', "Update adverse event report"),
            ('view_adverse_event', "View adverse event report"),
            ('create_blood_sample', "Create blood sample collection report"),
            ('update_blood_sample', "Update blood sample collection report"),
            ('view_blood_smaple', "View blood sample collection report"),
            ('create_consent', 'Create informaed consent'),
            ('update_consent', 'Update informaed consent'),
            ('view_consent', 'View informed consent'),
            ('create_compliance', 'Create compliance report'),
            ('update_compliance', 'Update compliance report'),
            ('view_compliance', 'View complaince report(s)'),
            ('create_final_questionnaire', 'Create final questionnaire'),
            ('update_final_questionnaire', 'Update final questionnaire'),
            ('view_final_questionnaire', 'View final questionnaire'),
            ('create_exit_interview', 'Create exit interview record'),
            ('update_exit_interview', 'Update exit interview record'),
            ('view_exit_interview', 'View exit interview(s)'),
            ('view_logs', "View logs of changes"),
        ]
