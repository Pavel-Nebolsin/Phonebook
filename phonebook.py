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

    def _load_data_from_file(self):
        try:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact(**self.convert_field_names(contact_data)) for contact_data in data]
        except FileNotFoundError:
            pass

    def _save_data_to_file(self):
        data = [self.convert_field_names(contact.to_dict(), reverse=True) for contact in self.contacts]
        with open(self.file_name, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def convert_field_names(self, contact_data, reverse=False):
        converted_data = {}
        field_mapping = self.field_name_mapping
        if reverse:
            field_mapping = {v: k for k, v in self.field_name_mapping.items()}
        for key, value in contact_data.items():
            converted_key = field_mapping.get(key, key)
            converted_data[converted_key] = value
        return converted_data

    def find_contacts(self, criteria):
        converted_criteria = self.convert_field_names(criteria)
        results = []
        matching_indices = []
        for index, contact in enumerate(self.contacts):
            match = True
            for key, value in converted_criteria.items():
                if value.strip():  # Проверяем, не является ли значение пустой строкой или строкой из пробелов
                    contact_value = contact.__dict__.get(key, "").lower()
                    if value.lower() not in contact_value:
                        match = False
                        break
            if match:
                results.append(contact)
                matching_indices.append(index)
        return results, matching_indices

    field_name_mapping = {
        "фамилия": "last_name",
        "имя": "first_name",
        "отчество": "middle_name",
        "название организации": "organization",
        "телефон рабочий": "work_phone",
        "телефон личный": "personal_phone"
    }
