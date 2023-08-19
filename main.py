from phonebook import PhoneBook
from console_ui import ConsoleUI
from contact import Contact


def main():
    run = True
    while run:
        phone_book = PhoneBook()
        run = ConsoleUI.run(phone_book)


if __name__ == "__main__":
    main()
