import math
import os
import sys

from contact import Contact


class UI:

    @staticmethod
    def input_data(mode='new'):
        if mode == 'filter':
            message = 'Введите значения параметров поиска (или нажмите Enter, чтобы не включать в поиск):'
        elif mode == 'edit':
            message = 'Введите новые значения (или нажмите Enter, чтобы оставить поле без изменений):'
        else:
            message = 'Введите данные нового контакта:'

        print(UI.text_color(message, 'yellow'))

        data = {'last_name': input("Фамилия: "),
                'first_name': input("Имя: "),
                'middle_name': input("Отчество: "),
                'organization': input("Организация: "),
                'work_phone': input("Телефон (рабочий): "),
                'personal_phone': input("Телефон (личный): ")}

        cleaned_data = {key: value.strip() for key, value in data.items()}

        return cleaned_data

    @staticmethod
    def display_contacts_list(contacts, indices=None, page=2, contacts_per_page=20):
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
                contact.last_name,
                contact.first_name,
                contact.middle_name,
                contact.organization,
                contact.work_phone,
                contact.personal_phone
            ]
            print(columns.format(*values))

        page_print = f'Страница №{page}'
        print('-' * len(header))
        print(' ' * ((len(header) // 2) - len(page_print)), UI.text_color(page_print, 'blue'))

    @staticmethod
    def text_color(message, color=None):
        if not color:
            return f'{message}'
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'reset': '\033[0m'
        }
        color_code = colors.get(color, colors['reset'])
        return f"{color_code}{message}{colors['reset']}"

    @staticmethod
    def display_message(message, color=None):
        print(UI.text_color(message, color))

    @staticmethod
    def validate_input_id(phone_book):
        while True:
            contact_index = input(UI.text_color('Введите ID контакта:', 'yellow'))
            try:
                contact_index = int(contact_index) - 1
                _ = phone_book.contacts[contact_index]
                return contact_index
            except ValueError:
                UI.display_message(f'Неверный формат ID (введите число)', 'red')
            except IndexError:
                UI.display_message(f'Введите ID от 1 до {len(phone_book.contacts)}', 'red')

    @staticmethod
    def search(phone_book):
        UI.move_cursor_up(1)
        search_data = UI.input_data(mode='filter')
        indices = phone_book.find_contacts(search_data)
        message = (f'По заданным критериям найдено {len(indices)} контактов: ', 'green') \
            if indices else ('По заданным критериям ничего не найдено: ', 'yellow')
        UI.display_message(*message)

        if indices:
            UI.paginator(phone_book.contacts, indices)

    @staticmethod
    def edit_contact(phone_book):

        contact_index = UI.validate_input_id(phone_book)

        UI.clear_console()
        contact_to_edit = phone_book.get_contact(contact_index)
        UI.display_message(f'Редактирование контакта:\n\n{contact_to_edit.display()}\n', 'yellow')

        new_data = UI.input_data(mode='edit')
        edited_contact = phone_book.edit_contact(contact_index, new_data)

        UI.show_contact_modal(edited_contact, 'изменён', 'green')

    @staticmethod
    def delete_contact(phone_book):

        contact_index = UI.validate_input_id(phone_book)

        UI.clear_console()
        contact_to_delete = phone_book.delete_contact(contact_index)

        UI.show_contact_modal(contact_to_delete, 'удалён', 'red')

    @staticmethod
    def add_contact(phone_book):
        UI.clear_console()
        new_contact = UI.input_data()
        contact = Contact(**new_contact)
        phone_book.add_contact(contact)
        UI.show_contact_modal(contact, 'добавлен', 'green')

    @staticmethod
    def show_contact_modal(contact, action, color):
        UI.clear_console()
        UI.display_message(f'Контакт успешно {action}:\n\n{contact.display()}\n', color)
        input('Нажмите Enter чтобы продолжить...')
        UI.clear_console()

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def move_cursor_up(lines):
        for _ in range(lines):
            sys.stdout.write('\033[F\033[K')  # Перемещаем курсор на строку вверх и очищаем строку
            sys.stdout.flush()

    @staticmethod
    def validate_paginator_values(value, max_value):
        try:
            value = int(value)

        except ValueError:
            UI.move_cursor_up(2)
            UI.display_message(f'Недопустимое значение, повторите ввод', 'red')
            return None

        clamped_value = max(1, min(value, max_value))
        return clamped_value

    @staticmethod
    def paginator(contacts, indices=None):
        length = len(indices) if indices else len(contacts)
        while True:
            contacts_per_page = input(UI.text_color(
                f'Введите количество контактов на странице (от 1 до {length}): ', 'blue'))

            validated_contacts_per_page = UI.validate_paginator_values(contacts_per_page, length)
            if validated_contacts_per_page:
                break

        UI.clear_console()
        UI.display_contacts_list(contacts, indices, 1, validated_contacts_per_page)

        while True:
            max_page = math.ceil(length / validated_contacts_per_page)

            if length > validated_contacts_per_page:
                UI.display_message(f'Нажмите Enter чтобы вернуться в главное Меню', 'yellow')
                page = input(UI.text_color(f'или выберете страницу от 1 до {max_page}: ', 'blue'))
            else:
                break

            if not page:
                UI.move_cursor_up(2)
                break

            validated_page_value = UI.validate_paginator_values(page, max_page)
            if not validated_page_value:
                continue

            UI.clear_console()
            UI.display_contacts_list(contacts, indices, validated_page_value, validated_contacts_per_page)

    @staticmethod
    def display_menu():
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
    def run(phone_book):
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
                input(UI.text_color('Некорректный выбор. Пожалуйста, '
                                    'выберите действие из меню.'
                                    '(Enter - продолжить)',
                                    'red'))
                UI.clear_console()
