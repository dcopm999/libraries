'''
package: libraries
description: Классы авторизации
'''
from libraries.patterns import Singleton

from libraries.models import Registration


class BaseAuth(Singleton):
    '''
    Класс авторизации:
    TODO
    '''
    def __init__(self):
        try:
            self._data = Registration.objects.all()[0]
        except IndexError:
            raise IndexError("Не задан регистрационный ключ")

    @property
    def get_token(self):
        '''
        Из Registration возвращает token подключения
        '''
        return self._data.token

    @property
    def get_host(self):
        '''
        Из Registration возвращает имя хоста для подключения
        '''
        return self._data.host
