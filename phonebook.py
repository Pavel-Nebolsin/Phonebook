import json
from contact import Contact


class PhoneBook:
    def __init__(self, data_file_path: str = 'data.json') -> None:
        self.contacts: list[Contact] = []
        self.data_file_path: str = data_file_path
        self._load_data_from_file()

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)
        self._save_data_to_file()

    def get_contact(self, contact_index: int) -> Contact | None:
        try:
            contact = self.contacts[contact_index]
            return contact
        except ValueError:
            return None

    def edit_contact(self, contact_index: int, new_data: dict[str, str]) -> Contact:
        contact = self.contacts[contact_index]
        contact.update(new_data)
        self._save_data_to_file()
        return contact

    def delete_contact(self, index: int) -> Contact:
        removed_contact = self.contacts.pop(index)
        self._save_data_to_file()
        return removed_contact

    def find_contacts(self, criteria: dict[str, str]) -> list[int]:
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
        try:
            with open(self.data_file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact(**contact_data) for contact_data in data]
        except FileNotFoundError:
            pass

    def _save_data_to_file(self) -> None:
        data = [contact.to_dict() for contact in self.contacts]
        with open(self.data_file_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def clear_data(self) -> None:
        self.contacts = []
        self._save_data_to_file()
