import random
import requests
from contact import Contact
from phonebook import PhoneBook


def fill_up_phonebook(requests_count: int = 1, contacts_per_request: int = 100, clear: bool = False) -> None:
    """
    Заполняет телефонный справочник случайными контактами из внешнего API.

    :param requests_count: Количество запросов к API для получения контактов.
    :param contacts_per_request: Количество контактов в одном запросе (максимум 100).
    :param clear: Флаг, указывающий на необходимость очистки данных в телефонном справочнике перед заполнением.
    """

    # Здесь можно добавить компании и их телефонные номера
    organizations_with_phones = [
        ("Effective Mobile", "+79123456789"),
        ("Yandex", "+79098765432"),
        ("Mail.ru", "+79111223344"),
        ("Google", "+79999887766"),
        ("Telegram", "+79887766554"),
        ("VK", "+79765432109"),
        ("Afterlogic", "+79453678901"),
        ("Ростех", "+79678901234"),
        ("Сбер", "+79321098765"),
        ("Тинькофф", "+79004456799")
    ]

    pb = PhoneBook()
    if clear:
        pb.clear_data()
    for _ in range(requests_count):
        api_url = f"https://api.randomdatatools.ru/?count={contacts_per_request}&params=LastName,FirstName,FatherName,Phone,Phone"
        response = requests.get(api_url)
        data = response.json()

        for item in data:
            phone_number = item['Phone']
            personal_phone = phone_number.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")

            organization, work_phone = random.choice(organizations_with_phones)

            contact = Contact(item['LastName'],
                              item['FirstName'],
                              item['FatherName'],
                              organization,
                              work_phone,
                              personal_phone)
            pb.add_contact(contact)


fill_up_phonebook(requests_count=3, contacts_per_request=100, clear=True)
