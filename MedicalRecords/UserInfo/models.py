from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

from localflavor.us.models import USStateField

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User (AbstractUser):
    username = None 
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class UserInfo (models.Model):
    PREFIX_CHOISES = {
        ('Mr.', 'Mister'),
        ('Mrs.', 'Missus'),
        ('Ms.', 'Miss'),
        ('Dr.', 'Doctor')
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prefix = models.CharField('Prefix', max_length=4, choices=PREFIX_CHOISES, blank=True)

    f_name = models.CharField('First name', max_length=50, blank=False)
    m_name = models.CharField('Middle name', max_length=50, blank=True)
    l_name = models.CharField('Last name', max_length=100, blank=False)

    phone = PhoneNumberField(null=False, blank=False, unique=True)
    dob = models.DateField('Date of Birth', blank=False)

    address_1 = models.CharField("Address", max_length=128)
    address_2 = models.CharField("Address continue", max_length=128, blank=True)

    city = models.CharField("City", max_length=64, default="Tacoma")
    state = USStateField("State", default="WA")
    zip_code = models.CharField("zip code", max_length=5, default="98490")

    is_insured = models.BooleanField('Has insurance', default=False)
    