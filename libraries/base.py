import logging
import asyncio
import json

from libraries import api
from libraries.patterns import ItemManager
from libraries.auth import BaseAuth


LOGGER = logging.getLogger(__name__)


class BaseManager(ItemManager):
    """
    Базовый класс
    self.URL нужно задавать в виде параметра в наследнике
    self.URI нужно задавать в виде параметра в наследнике
    self.command:
        (нужно задавать в виде параметра в наследнике)
         имеет значения 'get', 'post'
    """
    def __init__(self):
        '''
        Инициализация класса
        '''
        self._auth = BaseAuth()
        self.TOKEN = self._auth.get_token
        self.URL = self._auth.get_host
        self.headers = {'Content-Type': 'application/json'}
        self.headers['Authorization'] = 'token {}'.format(self.TOKEN)
        self.ssl = False
        self.items = self.get_list()

    def get_list(self):
        LOGGER.debug("Выполняем get запрос")
        result = asyncio.run(api.get(
            url="{0}{1}".format(self.URL, self.URI),
            ssl=self.ssl,
            headers=self.headers,
            #params=self.params
        ))
        return result

    def create_item(self, data):
        LOGGER.debug("Выполняем post запрос")
        result = asyncio.run(api.post(
            url="{0}{1}?format=json".format(self.URL, self.URI),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        return result

    def update_item(self, data):
        result = asyncio.run(api.put(
            url="{0}{1}{2}/?format=json".format(self.URL, self.URI, data['uuid']),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        return result

    def delete_item(self, data):
        result = asyncio.run(api.delete(
            url="{0}{1}{2}".format(self.URL, self.URI, data['uuid']),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        return result
