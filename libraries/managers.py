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
    URI = '/api/search/room/'
    AGENT_UUID = '50834ad3-cffa-4d97-ba0a-7c8145edced0'
