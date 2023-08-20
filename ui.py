import os

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
    def display_contacts_list(contacts, indices=None):
        columns = '{:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<16} | {:<16}'
        header = columns.format(
            'ID', 'Фамилия', 'Имя', 'Отчество', 'Организация', 'Телефон(рабочий)', 'Телефон(личный)'
        )
        print(header)
        print('-' * len(header))
                
        for index in indices or range(len(contacts)):
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
        print('-' * len(header))

    @staticmethod
    def text_color(message, color=None):
        if not color:
            print(f'{message}')
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'reset': '\033[0m'
        }
        color_code = colors.get(color, colors['reset'])
        return f"{color_code}{message}{colors['reset']}"

    @staticmethod
    def display_message(message, color=None):
        print(UI.text_color(message, color))

    @staticmethod
    def edit_contact(phone_book):
        contact_index = int(input(UI.text_color('Введите ID контакта для редактирования:','yellow'))) - 1

        if not phone_book.get_contact(contact_index):
            UI.display_message('Некорректный ID контакта', 'red')
            return UI.edit_contact(phone_book)

        UI.clear_console()
        contact_to_edit = phone_book.get_contact(contact_index)
        UI.display_message(f'Редактирование контакта:\n\n{contact_to_edit.display()}\n', 'yellow')

        new_data = UI.input_data(mode='edit')
        edited_contact = phone_book.edit_contact(contact_index, new_data)

        UI.show_contact_modal(edited_contact, 'изменён')

    @staticmethod
    def show_contact_modal(contact, action):
        UI.clear_console()
        UI.display_message(f'Контакт успешно {action}:\n\n{contact.display()}\n', 'green')
        input('Нажмите Enter чтобы продолжить...')
        UI.clear_console()

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def colored_text(text, color):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'reset': '\033[0m'
        }
        color_code = colors.get(color, colors['reset'])
        print(f"{color_code}{text}{colors['reset']}")

    @staticmethod
    def display_menu():
        print('Меню:')
        print('1. Вывести все контакты')
        print('2. Добавить контакт')
        print('3. Редактировать контакт')
        print('4. Поиск контакта')
        print('0. Выйти')

    @staticmethod
    def run(phone_book):
        while True:
            UI.display_menu()
            choice = input('Выберите действие: ')

            if choice == '1':
                UI.clear_console()
                UI.display_contacts_list(phone_book.contacts)

            elif choice == '2':
                UI.clear_console()
                new_contact = UI.input_data()
                contact = Contact(**new_contact)
                phone_book.add_contact(contact)
                UI.show_contact_modal(contact, 'добавлен')

            elif choice == '3':
                UI.edit_contact(phone_book)

            elif choice == '4':
                contact_data = UI.input_data(mode='filter')
                indices = phone_book.find_contacts(contact_data)
                UI.clear_console()
                message = (f'По заданным критериям найден {len(indices)} контактов: ', 'green') if indices \
                    else ('По заданным критериям ничего не найдено: ', 'yellow')
                UI.display_message(*message)

                if indices:
                    UI.display_contacts_list(phone_book.contacts, indices)

            elif choice == '0':
                print('Выход...')
                return 0

            else:
                UI.display_message(
                    'Некорректный выбор. Пожалуйста, выберите действие из меню.',
                    'red')
