"""
package: libraries
description: Модуль с реализацией aiohttp клиента
"""
import logging
import aiohttp
from aiohttp.client_exceptions import ClientResponseError

LOGGER = logging.getLogger(__name__)


async def get(**kwargs) -> dict:
    """
    Method GET request
    """
    count = None
    async with aiohttp.ClientSession() as session:
        LOGGER.debug("переданные параметры запроса: %s", kwargs)
        async with session.get(**kwargs) as response:
            if response.status == 200:
                result = await response.json()
                if result.get('results') is not None:
                    count = result.get('count')
                    result = result.get('results')
            elif response.status in list(range(400, 499)):
                result = await response.json()
                LOGGER.error(f'url: {response}, code: {response.status}, msg: {result}')
                raise ClientResponseError(
                    request_info=response.request_info,
                    history=response.history, status=response.status,
                    message=response, headers=response.headers)
            else:
                result = await response.json()
            LOGGER.debug("url запроса: %s", response.url)
            LOGGER.debug("код ответа: %d", response.status)
            LOGGER.debug("результат ответа от сервера: %s", result)
            return {'code': response.status, 'result': result, 'count': count}


async def post(**kwargs) -> dict:
    """
    Method POST request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.post(**kwargs) as response:
            if response.status == 200:
                result = await response.json()
            elif response.status in list(range(400, 499)):
                result = await response.json()
                LOGGER.error(f'url: {response}, code: {response.status}, msg: {result}')
                raise ClientResponseError(
                    request_info=response.request_info,
                    history=response.history, status=response.status,
                    message=response, headers=response.headers,
                    result=result)
            else:
                result = None
            LOGGER.debug("url запроса: %s", response.url)
            LOGGER.debug("код ответа: %d", response.status)
            LOGGER.debug("результат ответа от сервера: %s", result)
            return {'code': response.status, 'result': result}


async def put(**kwargs) -> dict:
    """
    Method PUT request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.put(**kwargs) as response:
            if response.status == 200:
                result = await response.json()
            elif response.status in list(range(400, 499)):
                result = await response.json()
                LOGGER.error(f'url: {response}, code: {response.status}, msg: {result}')
                raise ClientResponseError(
                    request_info=response.request_info,
                    history=response.history, status=response.status,
                    message=response, headers=response.headers,
                    result=result)
            else:
                result = None
            LOGGER.debug("url запроса: %s", response.url)
            LOGGER.debug("код ответа: %d", response.status)
            LOGGER.debug("результат ответа от сервера: %s", result)
            return {'code': response.status, 'result': result}


async def delete(**kwargs) -> dict:
    '''
    Method delete request
    '''
    async with aiohttp.ClientSession() as session:
        async with session.delete(**kwargs) as response:
            if response.status == 200:
                result = await response.json()
            elif response.status in list(range(400, 499)):
                result = response
                LOGGER.error(f'url: {response}, code: {response.status}, msg: {result}')
                raise ClientResponseError(
                    request_info=response.request_info,
                    history=response.history, status=response.status,
                    message=response, headers=response.headers)
            else:
                result = None
            LOGGER.debug("url запроса: %s", response.url)
            LOGGER.debug("код ответа: %d", response.status)
            LOGGER.debug("результат ответа от сервера: %s", result)
            return {'code': response.status, 'result': result}


async def head(**kwargs) -> dict:
    """
    Method HEAD request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.head(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(result)
            return result


async def options(**kwargs) -> dict:
    """
    Method OPTIONS request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.options(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(result)
            return result


async def patch(**kwargs) -> dict:
    """
    Method PATCH request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.patch(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(result)
            return result
