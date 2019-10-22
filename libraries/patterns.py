"""
Паттерны
"""


class Singleton:  # pylint: disable=too-few-public-methods
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class ItemManager:
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
        return repr([item for item in self.items])
