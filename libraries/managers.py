'''
package: libraries
description: Модуль с менеджерами взаимодействия с CoreAPI
'''
from libraries.base import BaseManager


class Manager(BaseManager):
    '''
    Менеджер управления записями country в CoreAPI
    '''
    URI = '/api/address/country/'
