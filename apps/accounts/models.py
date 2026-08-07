from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
'''
AbstractUser gives us Django's complete authentication system
'''

# Create your models here.


class Role(models.TextChoices):  ## Why TextChoies - Because prevents typing mistake
    SUPER_ADMIN = "SUPER_ADMIN","Super Admin"
    ADMIN = "ADMIN" ,"Admin"
    DEPARTMENT_HEAD = "DEPARTMENT_HEAD" ,"Department Head"
    TEAM_LEADER = "TEAM_LEADER" ,"Team Leader"
    EMPLOYEE = "EMPLOYEE","Employee"


class User(AbstractUser): # Why inherit? because no need to rebuild authentication.

    username = None  # Remove django's default username field

    email= models.EmailField(
            unique= True , db_index= True,
            blank= False,
            null = False,
            )
    role = models.CharField(max_length= 30,
                            choices= Role.choices,
                            default=Role.EMPLOYEE,
                            db_index=True,
                            help_text="Aplication role used for authorization",
                            )  # because of RBAC it means after login --> Role---> Authorization.
    objects  = UserManager() # Create manager
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


    def __str__(self):  # For admin panel Logs , Debuggin and shell everything becomes readable.
        return self.email

    class Meta:  
            ordering = ["email"]
            verbose_name = 'User'
            verbose_name_plural = "Users"