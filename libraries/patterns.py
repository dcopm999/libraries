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
