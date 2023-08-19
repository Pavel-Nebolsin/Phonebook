class Contact:
    def __init__(self, last_name="", first_name="", middle_name="", organization="", work_phone="", personal_phone=""):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}" \
               f" |  {self.organization}  |  {self.work_phone}" \
               f" |  {self.personal_phone}"

    def update(self, new_data):
        self.last_name = new_data['last_name'] if new_data.get('last_name', '') else self.last_name
        self.first_name = new_data['first_name'] if new_data.get('first_name', '') else self.first_name
        self.middle_name = new_data['middle_name'] if new_data.get('middle_name', '') else self.middle_name
        self.organization = new_data['organization'] if new_data.get('organization', '') else self.organization
        self.work_phone = new_data['work_phone'] if new_data.get('work_phone', '') else self.work_phone
        self.personal_phone = new_data['personal_phone'] if new_data.get('personal_phone', '') else self.personal_phone

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
