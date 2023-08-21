class Contact:
    def __init__(self, last_name: str = "", first_name: str = "", middle_name: str = "",
                 organization: str = "", work_phone: str = "", personal_phone: str = "") -> None:
        """
        Создание объекта контакта.

        :param last_name: Фамилия.
        :param first_name: Имя.
        :param middle_name: Отчество.
        :param organization: Организация.
        :param work_phone: Рабочий телефон.
        :param personal_phone: Личный телефон.
        """
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.organization: str = organization
        self.work_phone: str = work_phone
        self.personal_phone: str = personal_phone

    def __str__(self) -> str:
        """
        Получение строкового представления контакта.

        :return: Строковое представление контакта.
        """
        return f"{self.last_name} {self.first_name} {self.middle_name}" \
               f" |  {self.organization}  |  {self.work_phone}" \
               f" |  {self.personal_phone}"

    def update(self, new_data: dict) -> None:
        """
        Обновление данных контакта на основе новых данных.

        :param new_data: Новые данные для обновления.
        """
        self.last_name = new_data.get('last_name', '') or self.last_name
        self.first_name = new_data.get('first_name', '') or self.first_name
        self.middle_name = new_data.get('middle_name', '') or self.middle_name
        self.organization = new_data.get('organization', '') or self.organization
        self.work_phone = new_data.get('work_phone', '') or self.work_phone
        self.personal_phone = new_data.get('personal_phone', '') or self.personal_phone

    def to_dict(self) -> dict[str, str]:
        """
        Преобразование контакта в словарь.

        :return: Словарь с данными контакта.
        """
        return self.__dict__

    def display(self) -> str:
        """
        Получение строкового представления контакта
        для отображения в UI при изменении, добавлении или удалении.

        :return: Отформатированное строковое представление контакта.
        """
        return f"Фамилия: {self.last_name}\nИмя: {self.first_name}\nОтчество: {self.middle_name}\n" \
               f"Организация: {self.organization}\nТелефон (рабочий): {self.work_phone}\n" \
               f"Телефон (личный): {self.personal_phone}"
