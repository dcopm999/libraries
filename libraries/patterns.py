"""
package: libraries
description: Классы с паттернами
"""


class Singleton:  # pylint: disable=too-few-public-methods
    '''
    Реализация паттерна проектирования Singleton
    description: Гарантирует, что у класса есть только один экземпляр, и
    предоставляет к нему глобальную точку доступа.
    '''
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


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

    # def __repr__(self):
    #    return repr([item for item in self.items])


class ChainHandlerMixin:
    '''
    pattern: Цепочка обязанностей

    description: поведенческий паттерн, позволяющий 
    передавать запрос по цепочке потенциальных обработчиков, 
    пока один из них не обработает запрос
    '''
    def __init__(self, *args, **kwargs):
        super(ChainHandlerMixin, self).__init__(*args, **kwargs)
        
    def search(self, data:dict) -> str:
        """
        data: dict form search form
        """
        params = dict()
        filters = [getattr(self, item) for item in self.filters]
        for item in filters:
            result = item(data)
            if result:
                params.update(result)
        self.params = params
        print(self.params)
        return self.get_list()

    def multichoice_filter(self, data:dict) -> dict:
        result = dict()
        for key, value in data.items():
            if isinstance(value, list):
                result_key = f'{key}__in'
                for item in value:
                    if value.index(item) == 0:
                        result_value = f'{item}'
                    else:
                        result_value += f'__{item}'
                result[result_key] = result_value
        return result

    def daterange_filter(self, data:dict) -> dict:
        if data.get('date_start'):
            key = 'date__range'
            date_start = data.get('date_start')
            date_end = data.get('date_end')
            value = f'{date_start}__{date_end}'
            return {key: value}

    def city_filter(self, data:dict) -> dict:
        if data.get('city'):
            return {'city': data.get('city')}
