from django.db import models

# Create your models here.


class Registration(models.Model):
    host = models.CharField(max_length=250, verbose_name='URL')
    token = models.CharField(max_length=250, verbose_name='Ключ регистрации')

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'регистрационный ключ'
        verbose_name_plural = 'Регистрационные ключи'
