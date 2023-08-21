import math

from contact import Contact
from helpers import text_color, clear_console, move_cursor_up
from phonebook import PhoneBook


class UI:

    @staticmethod
    def input_data(mode: str = 'new') -> dict:
        if mode == 'filter':
            message = 'Введите значения параметров поиска (или нажмите Enter, чтобы не включать в поиск):'
        elif mode == 'edit':
            message = 'Введите новые значения (или нажмите Enter, чтобы оставить поле без изменений):'
        else:
            message = 'Введите данные нового контакта:'

        print(text_color(message, 'yellow'))

        data = {'last_name': input("Фамилия: "),
                'first_name': input("Имя: "),
                'middle_name': input("Отчество: "),
                'organization': input("Организация: "),
                'work_phone': input("Телефон (рабочий): "),
                'personal_phone': input("Телефон (личный): ")}

        cleaned_data = {key: value.strip() for key, value in data.items()}

        return cleaned_data

    @staticmethod
    def display_contacts_list(contacts: list[Contact], indices: list[int] | None = None,
                              page: int = 1, contacts_per_page: int = 20) -> None:
        columns = '{:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<16} | {:<16}'
        header = columns.format(
            'ID', 'Фамилия', 'Имя', 'Отчество', 'Организация', 'Телефон(рабочий)', 'Телефон(личный)'
        )
        print(header)
        print('-' * len(header))

        start_index = (page - 1) * contacts_per_page
        end_index = start_index + contacts_per_page

        indices = indices if indices else range(len(contacts))

        for index in indices[start_index:end_index]:
            contact = contacts[index]
            values = [
                index + 1,
                *list(contact.to_dict().values())
            ]
            print(columns.format(*values))

        page_print = f'Страница №{page}'
        print('-' * len(header))
        print(' ' * ((len(header) // 2) - len(page_print)), text_color(page_print, 'blue'))

    @staticmethod
    def display_message(message: str, color: str = None) -> None:
        print(text_color(message, color))

    @staticmethod
    def search(phone_book: PhoneBook) -> None:
        move_cursor_up(1)
        search_data = UI.input_data(mode='filter')
        indices = phone_book.find_contacts(search_data)
        if indices:
            UI.display_message(f'По заданным критериям найдено {len(indices)} контактов: ', 'green')
            UI.paginator(phone_book.contacts, indices)
        else:
            input(text_color('По заданным критериям ничего не найдено (Enter - продолжить): ', 'yellow'))
            clear_console()

    @staticmethod
    def edit_contact(phone_book: PhoneBook) -> None:
        contact_index = UI.validate_input_id(phone_book)

        clear_console()
        contact_to_edit = phone_book.get_contact(contact_index)
        UI.display_message(f'Редактирование контакта:\n\n{contact_to_edit.display()}\n', 'yellow')

        new_data = UI.input_data(mode='edit')
        edited_contact = phone_book.edit_contact(contact_index, new_data)

        UI.show_contact_modal(edited_contact, 'изменён', 'green')

    @staticmethod
    def delete_contact(phone_book: PhoneBook) -> None:
        contact_index = UI.validate_input_id(phone_book)

        clear_console()
        contact_to_delete = phone_book.delete_contact(contact_index)

        UI.show_contact_modal(contact_to_delete, 'удалён', 'red')

    @staticmethod
    def add_contact(phone_book: PhoneBook) -> None:
        clear_console()
        new_contact = UI.input_data()
        contact = Contact(**new_contact)
        phone_book.add_contact(contact)
        UI.show_contact_modal(contact, 'добавлен', 'green')

    @staticmethod
    def show_contact_modal(contact: Contact, action: str, color: str) -> None:
        clear_console()
        UI.display_message(f'Контакт успешно {action}:\n\n{contact.display()}\n', color)
        input('Нажмите Enter чтобы продолжить...')
        clear_console()

    @staticmethod
    def paginator(contacts: list[Contact], indices: list[int] | None = None) -> None:
        length = len(indices) if indices else len(contacts)
        while True:
            contacts_per_page = input(text_color(
                f'Введите количество контактов на странице (от 1 до {length}): ', 'blue'))

            validated_contacts_per_page = UI.validate_paginator_values(contacts_per_page, length)
            if validated_contacts_per_page:
                break

        clear_console()
        UI.display_contacts_list(contacts, indices, 1, validated_contacts_per_page)

        while True:
            max_page = math.ceil(length / validated_contacts_per_page)

            if length > validated_contacts_per_page:
                UI.display_message(f'Нажмите Enter чтобы вернуться в главное Меню', 'yellow')
                page = input(text_color(f'или выберете страницу от 1 до {max_page}: ', 'blue'))
            else:
                break

            if not page:
                move_cursor_up(2)
                break

            validated_page_value = UI.validate_paginator_values(page, max_page)
            if not validated_page_value:
                continue

            clear_console()
            UI.display_contacts_list(contacts, indices, validated_page_value, validated_contacts_per_page)

    @staticmethod
    def display_menu() -> None:
        menu_items = {
            '1': 'Вывести все контакты',
            '2': 'Добавить новый контакт',
            '3': 'Редактировать контакт',
            '4': 'Поиск по контактам',
            '5': 'Удалить контакт',
            '0': 'Выйти'
        }
        print('Меню:')
        for key, value in menu_items.items():
            print(f'{key}. {value}')

    @staticmethod
    def validate_input_id(phone_book: PhoneBook) -> int | None:
        while True:
            contact_index = input(text_color('Введите ID контакта:', 'yellow'))
            try:
                contact_index = int(contact_index) - 1
                _ = phone_book.contacts[contact_index]
                return contact_index
            except ValueError:
                move_cursor_up(2)
                UI.display_message(f'Неверный формат ID (введите число)', 'red')
            except IndexError:
                move_cursor_up(2)
                UI.display_message(f'Введите ID от 1 до {len(phone_book.contacts)}', 'red')

    @staticmethod
    def validate_paginator_values(value: str, max_value: int) -> int | None:
        try:
            value = int(value)

        except ValueError:
            move_cursor_up(2)
            UI.display_message(f'Недопустимое значение, повторите ввод', 'red')
            return None

        clamped_value = max(1, min(value, max_value))
        return clamped_value

    @staticmethod
    def run(phone_book: PhoneBook) -> int | None:
        while True:
            UI.display_menu()
            choice = input('\nВыберите действие: ')

            if choice == '1':
                UI.paginator(phone_book.contacts)

            elif choice == '2':
                UI.add_contact(phone_book)

            elif choice == '3':
                UI.edit_contact(phone_book)

            elif choice == '4':
                UI.search(phone_book)

            elif choice == '5':
                UI.delete_contact(phone_book)

            elif choice == '0':
                print('Выход...')
                return 0

            else:
                input(text_color('Некорректный выбор. Пожалуйста, '
                                 'выберите действие из меню.'
                                 '(Enter - продолжить)',
                                 'red'))
                move_cursor_up(10)
