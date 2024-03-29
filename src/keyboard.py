from src.item import Item

class Keyboard(Item):

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        if self.__language == "RU":
            self.__language = "EN"
        elif self.__language == "EN":
            self.__language = "RU"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_lang):
        print("""AttributeError: property 'language' of 'Keyboard' object has no setter""")
