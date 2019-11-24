'''
package: libraries
description: Модуль административной панели
'''
from django.contrib import admin

from libraries import models


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    '''
    Админка для параметров подключения к CoreAPI
    '''
    list_display = ['token']
