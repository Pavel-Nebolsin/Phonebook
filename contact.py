class Contact:
    def __init__(self, last_name="", first_name="", middle_name="",
                 organization="", work_phone="", personal_phone=""):
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
        self.last_name = new_data.get('last_name', '') or self.last_name
        self.first_name = new_data.get('first_name', '') or self.first_name
        self.middle_name = new_data.get('middle_name', '') or self.middle_name
        self.organization = new_data.get('organization', '') or self.organization
        self.work_phone = new_data.get('work_phone', '') or self.work_phone
        self.personal_phone = new_data.get('personal_phone', '') or self.personal_phone

    def to_dict(self):
        return self.__dict__

    def display(self):
        return f"Фамилия: {self.last_name}\nИмя: {self.first_name}\nОтчество: {self.middle_name}\n" \
               f"Организация: {self.organization}\nТелефон (рабочий): {self.work_phone}\n" \
               f"Телефон (личный): {self.personal_phone}"
