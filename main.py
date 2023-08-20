from phonebook import PhoneBook
from ui import UI
from contact import Contact


def main():
    run = True
    while run:
        UI.clear_console()
        phone_book = PhoneBook()
        run = UI.run(phone_book)


if __name__ == "__main__":
    main()
