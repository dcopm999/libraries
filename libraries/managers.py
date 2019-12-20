'''
package: libraries
description: Модуль с менеджерами взаимодействия с CoreAPI
'''
from libraries.base import BaseManager, BaseSearchManager
import logging

LOGGER = logging.getLogger(__name__)


class BaseFilterHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, data:dict, result:dict):
        if self._next_handler:
            LOGGER.debug('BaseFilterHandler.handle data: %s' % data)
            LOGGER.debug('BaseFilterHandler ressult: %s' % result)
            return self._next_handler.handle(data, result)
        else:
            LOGGER.debug('BaseFilterHandler self._next_handler: %s' % self._next_handler)
            LOGGER.debug('BaseFilterHandler.handle data: %s' % data)
            LOGGER.debug('BaseFilterHandler before ressult: %s' % result)
            return result

    def del_key(self, proc_keys:dict, data) -> None:
        for key in proc_keys.keys():
            del data[key]


class SubscribeFromFilterHandler(BaseFilterHandler):

    def handle(self, data:dict, result:dict = dict()) ->dict:
        LOGGER.debug('SubscribeFromFilterHandler.handle')
        hotel_list = list()
        proc_keys = dict(agent = None)
        manager = SubscribeSearchManager()
        manager.params = dict(contragent_from=data.get('agent'), is_approved='true')
        if not manager.get_list():
            hotel_list = ['None', ]
        else:
            for item in manager.get_list():
                hotel_list.append(item.get('contragent_to'))
        self.del_key(proc_keys, data)
        data.update({'hotel': hotel_list})
        LOGGER.debug('SubscribeFromFilterHandler result: %s ' % result)
        LOGGER.debug('SubscribeFromFilterHandler.handle data: %s ' % data)
        return super().handle(data, result)


class DaterangeFilterHandler(BaseFilterHandler):

    def handle(self, data:dict, result:dict=dict()) ->dict:
        LOGGER.debug('DaterangeFilterHandler.handle')
        LOGGER.debug('DaterangeFilterHandler data: %s' % data)
        proc_keys = dict(date_start=None, date_end=None)
        if data.get('date_start'):
            key = 'date__range'
            date_start = data.get('date_start')
            date_end = data.get('date_end')
            value = f'{date_start}__{date_end}'
            result[key]= value
        self.del_key(proc_keys, data)
        LOGGER.debug('DaterangeFilterHandler.handle result: %s ' % result)
        return super().handle(data, result)


class MultichoiceFilterHandler(BaseFilterHandler):

    def handle(self, data:dict, result:dict=dict()) ->dict:
        LOGGER.debug('MultichoiceFilterHandler.handle')
        LOGGER.debug('MultichoiceFilterHandler data %s' % data)
        LOGGER.debug('MultichoiceFilterHandler.handle result: %s ' % result)
        proc_keys = dict()
        for key, value in data.items():
            if isinstance(value, list) and len(value)>1:
                proc_keys[key] = None
                result_key = f'{key}__in'
                for item in value:
                    if value.index(item) == 0:
                        result_value = f'{item}'
                    else:
                        result_value += f'__{item}'
                result[result_key] = result_value
            elif isinstance(value, list) and len(value)==1:
                proc_keys[key] = None
                result[key] = value[0]
            elif isinstance(value, list):
                proc_keys[key] = None
        self.del_key(proc_keys, data)
        LOGGER.debug('MultichoiceFilterHandler.handle result: %s ' % result)
        return super(MultichoiceFilterHandler, self).handle(data, result)


class StrFilterHandler(BaseFilterHandler):

    def handle(self, data:dict, result:dict=dict()) ->dict:
        LOGGER.debug('StrFilterHandler.handle')
        proc_keys = dict()
        for key, value in data.items():
            if isinstance(value, str):
                result[key] = value
                proc_keys[key] = None
        self.del_key(proc_keys, data)
        LOGGER.debug('result: %s ' % result)
        return super().handle(data, result)


class BooleanFilterHandler(BaseFilterHandler):

    def handle(self, data:dict, result:dict=dict()) ->dict:
        LOGGER.debug('BooleanFilterHandler.handle')
        for key, value in data.items():
            if isinstance(value, bool):
                result[key] = str(value).lower()
                self.del_key(result, data)
        LOGGER.debug('result: %s ' % result)
        return super().handle(data, result)


class Manager(BaseManager):
    '''
    Менеджер управления записями country в CoreAPI
    '''
    URI = '/api/address/country/'


class TestSearchManager(BaseSearchManager):
    '''
    Менеджер управления поиском комнат в CoreAPI
    '''
    URI = '/api/search/reservation/'
    filters = BaseFilterHandler()
    filters.set_next(SubscribeFromFilterHandler()).set_next(MultichoiceFilterHandler()).set_next(DaterangeFilterHandler()).set_next(StrFilterHandler())


class SubscribeSearchManager(BaseSearchManager):
    '''
    Менеджер для поиска по подпискам
    '''
    URI = '/api/search/subscribe/'


class ReservationSearchManager(BaseSearchManager):
    '''
    Менеджер для поиска по броням
    '''
    URI = '/api/search/reservation/'


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    data = {'str': 'str', 'int': 1, 'list': ['1', '2'], 'date_start': '2019-12-01', 'date_end': '2019-12-05', 'agent': '9c181751-1e9e-4d87-a508-d115d1431d2f' }

    base_filter = BaseFilterHandler()

    subscribe_filter = SubscribeFilterHandler()
    multi_filter = MultichoiceFilterHandler()
    str_filter = StrFilterHandler()
    date_filter = DaterangeFilterHandler()


    base_filter.set_next(subscribe_filter).set_next(multi_filter).set_next(date_filter).set_next(str_filter)
    print(dir(base_filter))
    base_filter.handle(data)
    print(base_filter.result)
