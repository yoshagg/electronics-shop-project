from src.item import Item

class Keyboard(Item):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language

    def change_lang(self):
        if self.language == "RU":
            self.language = "EN"
        elif self.language == "EN":
            self.language = "RU"
        else:
            print('''AttributeError: property 'language' of 'Keyboard' object has no setter''')




