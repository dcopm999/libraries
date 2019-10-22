"""
Модуль управления ox-sys sell
"""
import logging
from datetime import datetime

from libraries.base import BaseManager


LOGGER = logging.getLogger(__name__)
DATETIME_FORMAT = "%m/%d/%Y, %H:%M:%S"


class SellListManager(BaseManager):
    uri = '/sells/list'
    command = 'get'
    params = {'finishedTime[max]': datetime.now().strftime(DATETIME_FORMAT)}


class SellCreateManager(BaseManager):
    uri = '/cashdesks/12/sells'
    command = 'get'
    params = None
