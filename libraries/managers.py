'''
package: libraries
description: Модуль с менеджерами взаимодействия с CoreAPI
'''
from libraries.base import BaseManager, BaseSearchManager


class Manager(BaseManager):
    '''
    Менеджер управления записями country в CoreAPI
    '''
    URI = '/api/address/country/'


class TestSearchManager(BaseSearchManager):
    '''
    Менеджер управления поиском комнат в CoreAPI
    '''
    URI = '/api/search/reservation/'
    filters = ['multichoice_filter', 'daterange_filter', 'city_filter', ]
