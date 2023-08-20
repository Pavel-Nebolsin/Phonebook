import json

from contact import Contact


class PhoneBook:
    def __init__(self, file_name='data.json'):
        self.contacts = []
        self.file_name = file_name
        self._load_data_from_file()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self._save_data_to_file()

    def get_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            contact = self.contacts[contact_index]
            return contact
        return False

    def edit_contact(self, contact_index, new_data):
        contact = self.contacts[contact_index]
        contact.update(new_data)
        self._save_data_to_file()
        return contact

    def _load_data_from_file(self):
        try:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact(**contact_data) for contact_data in data]
        except FileNotFoundError:
            pass

    def _save_data_to_file(self):
        data = [contact.to_dict() for contact in self.contacts]
        with open(self.file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def find_contacts(self, criteria):
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

    def clear_data(self):
        self.contacts = []  # Очищаем список контактов
        self._save_data_to_file()  # Сохраняем изменения в файле


