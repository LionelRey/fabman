from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    INSCRIPTION_STATE = [
        ('not member', 'not member'),
        ('subscribed', 'subscribed'),
        ('member', 'member')
    ]

    MEMBER_TYPE = [
        ('membre', 'membre'),
        ('etudiant', 'étudiant'),
        ('passif', 'passif'),
        ('angel', 'angel'),
        ('alias', 'alias de facturation'),
    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None, null=True, blank=True)
    name = models.CharField('Nom', max_length=200)
    surname = models.CharField('Prénom', max_length=200)
    address = models.CharField('Adresse', max_length=200, default=None, null=True, blank=True)
    locality = models.CharField('Localité', max_length=200, default=None, null=True, blank=True)
    npa = models.IntegerField('NPA', default=None, null=True, blank=True)
    rfid = models.CharField(max_length=200, default=None, null=True, blank=True)
    visa = models.CharField(max_length=3, default=None, null=True, blank=True, unique=True)
    mail = models.EmailField('Email', max_length=200, default=None, null=True, blank=True)
    phone_number = models.CharField('Téléphone', max_length=25, default=None, null=True, blank=True)
    is_member = models.BooleanField('Membre', default=False)
    is_resigned = models.BooleanField('Démission', default=False)
    is_staff = models.BooleanField('Animateur', default=False)
    is_committee = models.BooleanField('Comité', default=False)
    bank_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    iban = models.CharField(max_length=200, default=None, null=True, blank=True)
    inscription_state = models.CharField(max_length=20, choices=INSCRIPTION_STATE, default='not member')
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPE, default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Project(models.Model):
    name = models.CharField(max_length=200)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        if self.member:
            return f'{self.member.visa}/{self.name}'
        else :
            return f'{self.name}'


