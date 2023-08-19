class Contact:
    def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return f"Фамилия: {self.last_name}\nИмя: {self.first_name}\nОтчество: {self.middle_name}\n" \
               f"Организация: {self.organization}\nТелефон (рабочий): {self.work_phone}\n" \
               f"Телефон (личный): {self.personal_phone}"

    def update(self, new_data):
        self.last_name = new_data["фамилия"]
        self.first_name = new_data["имя"]
        self.middle_name = new_data["отчество"]
        self.organization = new_data["название организации"]
        self.work_phone = new_data["телефон рабочий"]
        self.personal_phone = new_data["телефон личный"]

    def to_dict(self):
        return {
            "фамилия": self.last_name,
            "имя": self.first_name,
            "отчество": self.middle_name,
            "название организации": self.organization,
            "телефон рабочий": self.work_phone,
            "телефон личный": self.personal_phone
        }

    def display(self):
        pass
