from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
    """Manage the User profile"""

    def create_user(self, phone, name, location, profile_picture, password=None):
        """Create a new user profile"""
        user = self.model(
                phone=phone,
                name=name,
                location=location,
                profile_picture=profile_picture,
            )
        user.set_password(password)
        user.save(using=self._db)

        return user

    # def create_user(self, phone, name, location, profile_picture, password=None):
    #     """Create a new user profile"""
    #     user = self.model(
    #             phone=phone,
    #             name=name,
    #             location=location,
    #             profile_picture=profile_picture,
    #         )
    #     user.set_password(password)
    #     user.save(using=self._db)
    #
    #     return user

    def create_superuser(self, phone, name, password):
        """Create a superuser"""
        user = self.model(
            phone=phone,
            name=name,
        )

        user.set_password(password)

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Set database for users"""
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, default='')
    profile_picture = models.ImageField(
                    max_length=None,
                    upload_to='profile_pics/',
                    default=None,
                    blank=True,
                    null=True
                )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def get_full_name(self):
        """Retrieve user full name"""
        return self.name
