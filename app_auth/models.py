from django.db import models
class User(models.Model):
    surname = models.CharField('фамилия', max_length=128)
    name = models.CharField('имя', max_length=128)
    username = models.CharField('ник', max_length=128)
    USERNAME_FIELD = 'username'
