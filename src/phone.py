from item import Item

class Phone(Item):
    simcards = 0

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Phone.simcards += 1


