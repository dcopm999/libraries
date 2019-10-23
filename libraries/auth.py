from libraries.patterns import Singleton

from libraries.models import Registration


class BaseAuth(Singleton):
    '''
    Класс авторизации:
    TODO
    '''
    def __init__(self):
        try:
            self._DATA = Registration.objects.all()[0]
        except IndexError:
            raise IndexError("Не задан регистрационный ключ")

    @property
    def get_token(self):
        return self._DATA.token

    @property
    def get_host(self):
        return self._DATA.host
