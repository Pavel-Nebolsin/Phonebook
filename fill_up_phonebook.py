import random

import requests

from contact import Contact
from phonebook import PhoneBook

api_url = "https://api.randomdatatools.ru/?count=100&params=LastName,FirstName,FatherName,Phone,Phone"
response = requests.get(api_url)
data = response.json()

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
pb.clear_data()

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
