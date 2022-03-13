from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        Group, PermissionsMixin
from django.utils import timezone


# from phonenumber_field.modelfields import PhoneNumberField


now = timezone.now


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given username and password."""
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Creates and saves a new User"""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('groups_id', 1)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using username instead of email"""
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_payer = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
