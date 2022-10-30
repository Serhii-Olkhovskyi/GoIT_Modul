"""
В модуле разработаны следующие классы:
    AddressBook - создание адресной книги
"""
from collections import UserDict


class AddressBook(UserDict):
    """
    Класс AddressBook, который наследуется от UserDict, и добавлена логика поиска по записям
    """

    def add_record(self, name, phone=None):
        """
        Добавление контакта в адресную книгу
        """
        name = Name(name)
        phone = Phone(phone)
        record = Record(name=name)
        record.add(phone)
        self.data[record.name.value] = record
        print(f'add contact: {record.name.value} is completed')

    def find_number(self, name):
        """
        Поиск номера по имени
        """
        if name in self.data:
            print(self.data[name])
        else:
            print('contacts not found')

    def change(self, name, new_phone):
        """
         Изменение контакта в адресной книге
        """

        if name in self.data:
            record = self.data.get(name)  # -> Record:
            record.remove(new_phone)


class Field:
    """
    Класс Field, который будет родительским для всех полей
    """

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        """
        pass
        """
        return self.__value

    @value.setter
    def value(self, new_value):
        """
        pass
        """
        self.__value = new_value


class Name(Field):
    """
    Создаем класс для имени контакта. Класс Name, обязательное поле с именем.
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Phone(Field):
    """
    Создаем класс для телефонного номера. Класс Phone, необязательное поле с телефоном
    """

    def __init__(self, value):
        super().__init__(value)
        self.value = value
    #
    # @Field.value.setter
    # def value(self, value):
    #     self.__value = self.vallide_phone(value)
    #
    # @staticmethod
    # def vallide_phone(phone):
    #     """
    #     pass
    #     """
    #     if len(phone) != 10 or len(phone) != 13:
    #         print('Phone must be 10 or 13 characters')
    #         return False
    #
    #     return phone


class Record:
    """
    Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей
    и хранения обязательного поля Name.
    """

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add(self, phone):
        """
        Метод для добавления объектов Phone
        """
        self.phones.append(phone)

    def remove(self, phone):
        """
        Метод для редактирования объектов Phone
        """
        self.phones = []
        self.add(Phone(phone))

    def __repr__(self):
        return f"{', '.join([phone.value for phone in self.phones])}"