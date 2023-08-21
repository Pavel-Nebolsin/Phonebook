class Contact:
    def __init__(self, last_name: str = "", first_name: str = "", middle_name: str = "",
                 organization: str = "", work_phone: str = "", personal_phone: str = "") -> None:
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.organization: str = organization
        self.work_phone: str = work_phone
        self.personal_phone: str = personal_phone

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}" \
               f" |  {self.organization}  |  {self.work_phone}" \
               f" |  {self.personal_phone}"

    def update(self, new_data: dict) -> None:
        self.last_name = new_data.get('last_name', '') or self.last_name
        self.first_name = new_data.get('first_name', '') or self.first_name
        self.middle_name = new_data.get('middle_name', '') or self.middle_name
        self.organization = new_data.get('organization', '') or self.organization
        self.work_phone = new_data.get('work_phone', '') or self.work_phone
        self.personal_phone = new_data.get('personal_phone', '') or self.personal_phone

    def to_dict(self) -> dict[str, str]:
        return self.__dict__

    def display(self) -> str:
        return f"Фамилия: {self.last_name}\nИмя: {self.first_name}\nОтчество: {self.middle_name}\n" \
               f"Организация: {self.organization}\nТелефон (рабочий): {self.work_phone}\n" \
               f"Телефон (личный): {self.personal_phone}"
