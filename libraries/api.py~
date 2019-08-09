"""
Модуль с реализацией aiohttp клиента
"""
import logging
import aiohttp


LOGGER = logging.getLogger(__name__)


async def get(**kwargs) -> dict:
    """
    Method GET request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug("переданные параметры запроса: %s" % kwargs)
        async with session.get(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(response.status)
            LOGGER.debug("url запроса: %s" % response.url)
            LOGGER.debug("результат ответа от сервера: %s" % result)
            return result


async def post(**kwargs) -> dict:
    """
    Method POST request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.post(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(response.status)
            return result


async def put(**kwargs) -> dict:
    """
    Method PUT request
    """
    async with aiohttp.ClientSession() as session:
        LOGGER.debug(kwargs)
        async with session.put(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(result)
            return result


async def delete(**kwargs) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.delete(**kwargs) as response:
            result = await response.json()
            LOGGER.debug(result)
            return result


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
