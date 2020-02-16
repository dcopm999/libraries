"""
package: libraries
description: Классы с паттернами
"""
import logging

LOGGER = logging.getLogger(__name__)


class Singleton:  # pylint: disable=too-few-public-methods, attribute-defined-outside-init, no-member
    '''
    Реализация паттерна проектирования Singleton
    description: Гарантирует, что у класса есть только один экземпляр, и
    предоставляет к нему глобальную точку доступа.
    '''
    def __call__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class ItemManager:
    '''
    Реализация паттерна проектирования Prototype
    description: Паттерн прототип, а именно — из каких классов он состоит,
    какие роли эти классы выполняют и как они взаимодействуют друг с другом.
    '''
    items = list()

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        try:
            return self.items[index]
        except KeyError:
            return None

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        return map(lambda item: item, self.items)

    def __repr__(self):
        return repr(self.items)


class ChainHandlerMixin: # pylint: disable=too-few-public-methods
    '''
    pattern: Цепочка обязанностей

    description: поведенческий паттерн, позволяющий
    передавать запрос по цепочке потенциальных обработчиков,
    пока один из них не обработает запрос
    '''

    def search(self, data: dict) -> list:
        """
        data: dict form search form
        """
        self.params = {}
        LOGGER.debug('ChainHandlerMixin.search data: %s', data)
        self.params = self.filters.handle(data, result={})
        LOGGER.debug('ChainHandlerMixin.search params: %s', self.params)
        return self.get_list()
