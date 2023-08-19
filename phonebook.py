import json

from contact import Contact


class PhoneBook:
    def __init__(self, file_name='data.json'):
        self.contacts = []
        self.file_name = file_name
        self.load_data_from_file()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_data_to_file()

    def search_contacts(self, criteria):
        pass

    def edit_contact(self, contact, new_data):
        pass

    def load_data_from_file(self):
        try:
            with open(self.file_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact(**self.convert_field_names(contact_data)) for contact_data in data]
        except FileNotFoundError:
            pass

    def save_data_to_file(self):
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

    field_name_mapping = {
        "фамилия": "last_name",
        "имя": "first_name",
        "отчество": "middle_name",
        "название организации": "organization",
        "телефон рабочий": "work_phone",
        "телефон личный": "personal_phone"
    }
