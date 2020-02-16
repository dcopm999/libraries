# coding: utf-8
'''
package: libraries
description: Authorization classes

Example:
    import asyncio

    data = {
        'url': 'http://127.0.0.1:8000/ru/api/auth/jwt/',
        'url_verify': 'http://127.0.0.1:8000/ru/api/auth/jwt/verify/',
        'url_refresh': 'http://127.0.0.1:8000/ru/api/auth/jwt/refresh/',
        'username': 'admin',
        'password': '123456',
    }

    auth = JWTAuth(**data)
    asyncio.run(auth.login())


'''
import json
import logging
from libraries import (api, patterns)

LOGGER = logging.getLogger(__name__)


class JWTAuth(patterns.Singleton):
    '''
    desc: Provide generic JWT authentication class
    '''

    def __init__(self, **kwargs) -> None:
        '''
        Attributes:
            url (str): url path for connecting to jwt authentication backend
            url_verify (str): полный url для проверки токена
            url_refresh (str): полный url для обнвления токена
            username (str): логин
            password (str): пароль
            ssl (bool): устанавливать ssl соединение?
        '''
        self.url = kwargs.get('url', '')
        self.url_verify = kwargs.get('url_verify', '')
        self.url_refresh = kwargs.get('url_refresh', '')

        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')

        self.token = kwargs.get('token')
        self.token_refresh = kwargs.get('token_refresh')

        self.headers = {'content-type': 'application/json'}
        self.payload = {'username': self.username, 'password': self.password}

        self.is_authorized = None
        self.ssl = kwargs.get('ssl')


    async def _token_get(self) -> dict:
        '''
        Асинхронный метод получения токена по логину и паролю
        результат: возвращает словарь.
        {
        'code': 200,
        'result': {
            'refresh': 'eyJ0eXAiOiJKV1...',
            'access':  'eyJ0eXAiOiJKV1...',
            }
        }
        '''
        return await api.post(
            url=self.url,
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps(self.payload)
        )

    async def _token_refresh(self) -> dict:
        '''
        '''
        return await api.post(
            url=self.url_refresh,
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps({'refresh': self.token_refresh})
        )

    async def _token_verity(self) -> dict:
        '''
        '''
        return await api.post(
            url=self.url_verify,
            ssl=self.ssl,
            headers=self.headers,
            data=json.dumps({'token': self.token})
        )

    async def login(self) -> None:
        '''
        async method authentication
        '''
        if self.token is not None and self.token_refresh is not None:
            LOGGER.debug('veryfy token')
            response = await self._token_verity()

        elif self.token is None and self.token_refresh is not None:
            LOGGER.debug('refresh token')
            response = await self._token_refresh()

        elif self.token is None and self.token_refresh is None:
            LOGGER.debug('get token')
            response = await self._token_get()


        if response['code'] == 200:
            self.token = response['result']['access']
            self.token_refresh = response['result']['refresh']
            self.is_authorized = True
        else:
            self.token = False
            self.token_refresh = False
            self.is_authorized = False
