from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from localflavor.us.models import USStateField

class UserInfo (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    dob = models.DateField('Date of Birth', blank=False)

    address_1 = models.CharField("Address", max_length=128)
    address_2 = models.CharField("Address continue", max_length=128, blank=True)

    city = models.CharField("City", max_length=64, default="Tacoma")
    state = USStateField("State", default="WA")
    zip_code = models.CharField("zip code", max_length=5, default="98490")

    is_insured = models.BooleanField('Has insurance', default=False)
    