from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            print('Складывать можно только Phone и Item')

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, param):
        if param < 1 or param > 2 or param is float:
            print('Количество физических SIM-карт должно быть целым числом больше нуля.')
            raise ValueError
        else:
            self._number_of_sim = param

