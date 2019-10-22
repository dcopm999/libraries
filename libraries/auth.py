from libraries.patterns import Singleton

from libraries.models import Registration


class BaseAuth(Singleton):
    '''
    Класс авторизации:
    TODO
    '''
    def __init__(self):
        self._DATA = Registration.objects.all()[0]

    @property
    def get_token(self):
        return self._DATA.token

    @property
    def get_host(self):
        return self._DATA.host
