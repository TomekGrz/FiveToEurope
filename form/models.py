from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.forms import forms


class ClientDetails(models.Model):
    name = models.CharField(max_length=64, verbose_name='What is your full name, including middle names?')
    surname = models.CharField(max_length=64, verbose_name='Your surname:')
    date_of_birth = models.DateField(verbose_name='Date of birth (YYYY-MM-DD)')
    place_of_birth = models.CharField(max_length=128, verbose_name='Place of birth')
    date_of_mariage = models.DateField(verbose_name='Date of birth (YYYY-MM-DD)')
    place_of_mariage = models.CharField(max_length=128, verbose_name='Place of mariage')
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FemaleParentDetails(models.Model):
    name = models.CharField(max_length=64, verbose_name='Mothers name')
    surname = models.CharField(max_length=64, verbose_name='Mothers surname')
    date_of_birth = models.DateField(verbose_name='Date of birth (YYYY-MM-DD)')
    place_of_birth = models.CharField(max_length=128, verbose_name='Place of birth')
    date_of_mariage = models.DateField(verbose_name='Date of mariage (YYYY-MM-DD)')
    place_of_mariage = models.CharField(max_length=128, verbose_name='Place of mariage')
    maiden_name = models.CharField(max_length=128, verbose_name='Your mother maiden name')
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MaleParentDetails(models.Model):
    name = models.CharField(max_length=64, verbose_name='Fathers name')
    surname = models.CharField(max_length=64, verbose_name='Fathers surname')
    date_of_birth = models.DateField(verbose_name='Date of birth (YYYY-MM-DD)')
    place_of_birth = models.CharField(max_length=128, verbose_name='Place of birth')
    date_of_mariage = models.DateField(verbose_name='Date of mariage (YYYY-MM-DD)')
    place_of_mariage = models.CharField(max_length=128, verbose_name='Place of mariage')
    military_service = models.CharField(max_length=128, verbose_name='Has your father served in army? If yes, then which country?')
    occupation_before_51 = models.CharField(max_length=128, verbose_name='What was your father occupation before 1951?')
    # child = models.OneToOneField(ClientDetails, on_delete=models.CASCADE, blank=True)
    # wife = models.OneToOneField(FemaleParentDetails, on_delete=models.CASCADE, blank=True)
    # child = models.CharField(max_length=128)
    # wife = models.CharField(max_length=128)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    citizenship = models.BooleanField(default=None, verbose_name='Citizenship acquisition')
    research = models.BooleanField(default=None, verbose_name='Citizenship research')
    grant = models.BooleanField(default=None, verbose_name='Citizenship by grant')
    eligibility = models.BooleanField(default=None, verbose_name='Eligibility check')
    comment = models.TextField(max_length=900, null=True, verbose_name='Any additional comments')
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SupportPerson(models.Model):
    sup1 = models.BooleanField(verbose_name='Barbara')
    sup2 = models.BooleanField(verbose_name='Dorota')
    sup3 = models.BooleanField(verbose_name='Marta')
    support_person = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class CaseDescription(models.Model):
    free_text = models.TextField(max_length=1024,verbose_name='Describe your case')
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    q1_last_relative_left_poland = models.CharField(max_length=128, verbose_name='Name and surname of last know relative that lived in Poland')
    q2_next_destination = models.CharField(max_length=128, verbose_name='Where did this last relative lived afterwards?')
    q3_other_citizenships = models.CharField(max_length=128, verbose_name='Do you hold additional citizenships? If yes, which ones?')
    q4_granfather_army = models.CharField(max_length=128, verbose_name='Did your grandfather served in any army?')
    q5_grandfather_profession = models.CharField(max_length=128, verbose_name='What was your grandfather profession')
    q6_family_in_poland = models.CharField(max_length=128, verbose_name='Any remaining relatives still live in Poland?')
    q7_polish_docs = models.CharField(max_length=128, verbose_name='Please list all related documents that you have')
    q8_addoption = models.CharField(max_length=128, verbose_name='Were you adopted?')
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    phone = models.CharField(max_length=12, verbose_name='Please provide your phone number')
    email = models.EmailField(verbose_name='Please provide your contact email address')
    cbp = models.BooleanField(default=None, verbose_name='Preferred contact by phone?')
    cbe = models.BooleanField(default=None, verbose_name='Preferred contact by email?')
    day = models.DateField(auto_now_add=True)
    # time = models.TimeField(auto_now_add=True)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DocUpload(models.Model):
    description = models.CharField(max_length=64)
    doc = models.FileField()
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name