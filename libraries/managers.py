'''
package: libraries
description: Модуль с менеджерами взаимодействия с CoreAPI
'''
from libraries.base import BaseManager


class Manager(BaseManager):
    '''
    Менеджер управления записями country в CoreAPI
    '''
    URI = '/api/address/country/'


class SearchManager(BaseManager):
    '''
    Менеджер взаимодействия c поисковиком
    '''
    URI = '/api/search/room/'

    def search_param(self, params) -> None:
        '''
        params: dict from form.cleaned_data
        '''
        # Инициализируем переменную результата
        result = dict()
        # Итерация по словарю с возвращающая ключ,значение
        for key, values in params.items():
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
