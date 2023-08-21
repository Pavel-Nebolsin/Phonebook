from helpers import clear_console
from phonebook import PhoneBook
from ui import UI


def main() -> None:
    run = True
    while run:
        clear_console()
        phone_book = PhoneBook()
        run = UI.run(phone_book)


if __name__ == "__main__":
    main()
