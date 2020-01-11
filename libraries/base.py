'''
package: libraries.base
description: Набор классов прородителей  предназначенные для взаимодействия с RestAPI
'''
import logging
import asyncio
import json

from libraries import api
from libraries.patterns import ItemManager, ChainHandlerMixin
from libraries.auth import BaseAuth


LOGGER = logging.getLogger(__name__)


class BaseManager(ItemManager):
    # pylint: disable=too-many-instance-attributes
    '''
    Базовый класс
    self.url можно задавать в виде параметра в наследнике
    self.URI нужно задавать в виде параметра в наследнике
    '''
    URI = None

    def __init__(self):
        '''
        Инициализация класса
        '''
        self._auth = BaseAuth()
        self.token = self._auth.get_token
        self.url = self._auth.get_host
        self.headers = {'Content-Type': 'application/json'}
        self.headers['Authorization'] = 'token {}'.format(self.token)
        self.ssl = False
        self.code = 0
        self.params = dict()

    def get_list(self) -> list:
        '''
        Возвращает список элеметов API
        '''
        LOGGER.debug("Выполняем get запрос")
        result = asyncio.run(api.get(
            url="{0}{1}".format(self.url, self.URI),
            ssl=self.ssl,
            headers=self.headers,
            params=self.params
        ))
        self.items = result.get('result')
        self.code = result.get('code')
        self.count = result.get('count')
        return self.items

    def get_item_by_uuid(self, uuid) -> dict:
        '''
        Получение из API данных по UUID объекта
        '''
        LOGGER.debug("Выполняем get запрос")
        result = asyncio.run(api.get(
            url="{0}{1}{2}/?format=json".format(self.url, self.URI, uuid),
            ssl=self.ssl,
            headers=self.headers,
        ))
        self.code = result.get('code')
        return result.get('result')

    def create_item(self, data) -> dict:
        '''
        Создание записи в API
        '''
        LOGGER.debug("Выполняем post запрос")
        result = asyncio.run(api.post(
            url="{0}{1}?format=json".format(self.url, self.URI),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        self.code = result.get('code')
        self.items = self.get_list()
        return result.get('result')

    def update_item(self, data) -> dict:
        '''
        Обновление записи в API
        '''
        result = asyncio.run(api.put(
            url="{0}{1}{2}/?format=json".format(self.url, self.URI, data['uuid']),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        self.code = result.get('code')
        self.items = self.get_list()
        return result.get('result')

    def delete_item(self, data) -> dict:
        '''
        Удаление записи из API
        '''
        result = asyncio.run(api.delete(
            url="{0}{1}{2}".format(self.url, self.URI, data['uuid']),
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(data)
        ))
        self.code = result.get('code')
        return result.get('result')

    def update_or_create(self, data) -> dict:
        '''
        Обновление в случае присутствия или или создание новой записи в API
        '''
        self.items = self.get_list()
        if True in [data.get('uuid') in item.get('uuid') for item in self.items]:
            LOGGER.info('Обновление записи')
            result = self.update_item(data)
        else:
            LOGGER.info('Создание записи')
            result = self.create_item(data)
        self.items = self.get_list()
        return result


class BaseSearchManager(ChainHandlerMixin, BaseManager):
    '''
    Менеджер взаимодействия c поисковиком
    URI: путь в API к определенному поиску
    AGENT_UUID: uuid агента для проверки подписок в subscribe
    '''

    def search_param(self, data) -> None:
        '''
        data: dict from form.cleaned_data
        '''
        # Инициализируем переменную результата
        result = dict()
        # Итерация по словарю с возвращающая ключ,значение
        for key, values in data.items():

            # если тип занчения == список
            if isinstance(values, list):
                # Изменяем имя ключа для поиска в ElasticSearch по списку
                k = f'{key}__in'
                # Инициализация переменной с параметрами поиска
                result_value = str()
                # итерация по списку значений
                for value in values:
                    # Если текущее значение из списка является первым в списке
                    if value == values[0]:
                        # присвоение значения для первого элемента списка
                        result_value = f'{value}'
                    else:
                        # присвоение значений ля последующих элементов списка
                        result_value += f'__{value}'
                result[k] = result_value

            if isinstance(values, str): # ксди тип значения == str
                result[key] = values # присвоение значения в исходном виде
        self.params = result
