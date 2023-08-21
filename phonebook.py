import json
from contact import Contact


class PhoneBook:
    def __init__(self, data_file_path: str = 'data.json') -> None:
        """
        Инициализация телефонной книги.

        :param data_file_path: Путь к файлу, в котором хранятся данные о контактах.
        """
        self.contacts: list[Contact] = []
        self.data_file_path: str = data_file_path
        self._load_data_from_file()

    def add_contact(self, contact: Contact) -> None:
        """
        Добавление нового контакта в телефонную книгу.

        :param contact: Объект контакта для добавления.
        """
        self.contacts.append(contact)
        self._save_data_to_file()

    def get_contact(self, contact_index: int) -> Contact | None:
        """
        Получение контакта по индексу.

        :param contact_index: Индекс контакта в списке.
        :return: Объект контакта или None, если индекс недействителен.
        """
        try:
            contact = self.contacts[contact_index]
            return contact
        except ValueError:
            return None

    def edit_contact(self, contact_index: int, new_data: dict[str, str]) -> Contact:
        """
        Редактирование контакта.

       :param contact_index: Индекс контакта в списке.
       :param new_data: Словарь с новыми данными для обновления контакта.
       :return: Обновленный объект контакта.
       """
        contact = self.contacts[contact_index]
        contact.update(new_data)
        self._save_data_to_file()
        return contact

    def delete_contact(self, index: int) -> Contact:
        """
        Удаление контакта из телефонной книги.

        :param index: Индекс контакта для удаления.
        :return: Удаленный объект контакта.
        """
        removed_contact = self.contacts.pop(index)
        self._save_data_to_file()
        return removed_contact

    def find_contacts(self, criteria: dict[str, str]) -> list[int]:
        """
        Поиск контактов по заданным критериям.

        :param criteria: Словарь с критериями поиска.
        :return: Список индексов контактов, соответствующих критериям.
        """
        matching_indices = []
        for index, contact in enumerate(self.contacts):
            match = True
            for key, value in criteria.items():
                if value.strip():  # Проверяем, не является ли значение пустой строкой или строкой из пробелов
                    contact_value = contact.__dict__.get(key, "").lower()
                    if value.lower() not in contact_value:
                        match = False
                        break
            if match:
                matching_indices.append(index)
        return matching_indices

    def _load_data_from_file(self) -> None:
        """
        Загрузка данных о контактах из файла.

        Это внутренний метод и не предназначен для прямого вызова.
        """
        try:
            with open(self.data_file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact(**contact_data) for contact_data in data]
        except FileNotFoundError:
            pass

    def _save_data_to_file(self) -> None:
        """
        Сохранение данных о контактах в файл.

        Это внутренний метод и не предназначен для прямого вызова.
        """
        data = [contact.to_dict() for contact in self.contacts]
        with open(self.data_file_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def clear_data(self) -> None:
        """
        Очистка всех данных в телефонной книге.

        Все контакты будут удалены, и данные будут сохранены в файле.
        """
        self.contacts = []
        self._save_data_to_file()

