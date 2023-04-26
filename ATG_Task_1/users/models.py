from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    PATIENT, DOCTOR = 1, 2
    Type = models.PositiveSmallIntegerField(choices=((PATIENT, 'Patient'),
                                                     (DOCTOR, 'Doctor'),), default=PATIENT)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(verbose_name="Address", max_length=250)
    zip = models.CharField(verbose_name="Pin Code", max_length=10)
    ph = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.username


class PProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name="pprofile", on_delete=models.CASCADE)
    Occupation = models.CharField(max_length=100)
    i_company_name = models.CharField(verbose_name="Insurance Company Name", max_length=100)
    symptom = models.CharField(verbose_name="Symptom", max_length=100)


class DProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name="dprofile", on_delete=models.CASCADE)
    exp_in_years = models.CharField(verbose_name="Experience(in years)", max_length=100)
    edu = models.CharField(verbose_name="Education", max_length=100)
    awards = models.CharField(verbose_name="Awards", max_length=100)
    fee_charged = models.DecimalField(verbose_name="Fee (pre hour)", max_digits=7, decimal_places=2)

