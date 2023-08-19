from phonebook import PhoneBook
from console_ui import ConsoleUI
from contact import Contact


def main():
    phone_book = PhoneBook()
    run = True
    while run:
        phone_book = PhoneBook()
        run = ConsoleUI.run(phone_book)


if __name__ == "__main__":
    main()
