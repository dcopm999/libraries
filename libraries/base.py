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
    self.URL можно задавать в виде параметра в наследнике
    self.URI нужно задавать в виде параметра в наследнике
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
        self.code = 0
        self.params = dict()
        self.items = self.get_list()

    def get_list(self) -> list:
        '''
        Возвращает список элеметов API
        '''
        LOGGER.debug("Выполняем get запрос")
        result = asyncio.run(api.get(
            url="{0}{1}".format(self.URL, self.URI),
            ssl=self.ssl,
            headers=self.headers,
            params=self.params
        ))
        self.code = result.get('code')
        return result.get('result')

    def get_item_by_uuid(self, uuid) -> dict:
        LOGGER.debug("Выполняем get запрос")
        result = asyncio.run(api.get(
            url="{0}{1}{2}/?format=json".format(self.URL, self.URI, uuid),
            ssl=self.ssl,
            headers=self.headers,
        ))
        self.code = result.get('code')
        return result.get('result')

    def create_item(self, data) -> dict:
        LOGGER.debug("Выполняем post запрос")
        result = asyncio.run(api.post(
            url="{0}{1}?format=json".format(self.URL, self.URI),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        self.code = result.get('code')
        self.items = self.get_list()
        return result.get('result')

    def update_item(self, data) -> dict:
        result = asyncio.run(api.put(
            url="{0}{1}{2}/?format=json".format(self.URL, self.URI, data['uuid']),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        self.code = result.get('code')
        self.items = self.get_list()
        return result.get('result')

    def delete_item(self, data) -> dict:
        result = asyncio.run(api.delete(
            url="{0}{1}{2}".format(self.URL, self.URI, data['uuid']),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        self.code = result.get('code')
        return result.get('result')

    def update_or_create(self, data) -> dict:
        self.items = self.get_list()
        if True in [data.get('uuid') in item.get('uuid') for item in self.items]:
            LOGGER.info('Обновление записи')
            result = self.update_item(data)
        else:
            LOGGER.info('Создание записи')
            result = self.create_item(data)
        self.items = self.get_list()
        return result
