import csv
import pd

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[0:9]
        else:
            self.__name = new_name
        return 0

    def instantiate_from_csv(self, csv_file_name):
        data = pd.read_csv(csv_file_name, skiprows=1, sep=';', index_col=False,
                           names=["CSV_Item1", "CSV_Item2", "CSV_Item3", "CSV_Item4", 'CSV_Item5'])
        for _, row in data.iterrows():
            self.csvitem1 = row['CSV_Item1']
            self.csvitem2 = row['CSV_Item2']
            self.csvitem3 = row['CSV_Item3']
            self.csvitem4 = row['CSV_Item4']
            self.csvitem5 = row['CSV_Item5']
        return 0

    def string_to_number(self, param):
        return int(param)

