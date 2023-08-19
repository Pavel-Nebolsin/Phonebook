import os

from contact import Contact


class ConsoleUI:

    @staticmethod
    def input_data(mode='new'):
        if mode == 'filter':
            print("Введите значения для поиска (Enter - не включать в поиск):")
        elif mode == 'edit':
            print("Введите новые значения (Enter - чтобы оставить поле без изменений):")
        elif mode == 'new':
            print("Введите данные нового контакта:")

        new_contact = {'last_name': input("Фамилия: "),
                       'first_name': input("Имя: "),
                       'middle_name': input("Отчество: "),
                       'organization': input("Организация: "),
                       'work_phone': input("Телефон (рабочий): "),
                       'personal_phone': input("Телефон (личный): ")}

        return new_contact

    @staticmethod
    def input_search_criteria():

        pass

    @staticmethod
    def display_contacts(contacts, indexes=None):
        columns = '{:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<16} | {:<16}'
        header = columns.format(
            'ID', 'Фамилия', 'Имя', 'Отчество', 'Организация', 'Телефон(рабочий)', 'Телефон(личный)'
        )
        print(header)
        print('-' * len(header))

        for index in indexes or range(len(contacts)):
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
    def display_search_results(results):
        pass

    @staticmethod
    def display_message(message, color=None):
        if not color:
            print(f'*{message}*')
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
        print(f"{color_code}*{message}*{colors['reset']}")

    @staticmethod
    def edit_contact(phone_book):
        contact_index = int(input('Введите ID контакта для редактирования: ')) - 1

        if not phone_book.get_contact(contact_index):
            ConsoleUI.display_message('Некорректный номер контакта', 'red')
            return

        new_data = ConsoleUI.input_data(mode='edit')
        phone_book.edit_contact(contact_index, new_data)
        ConsoleUI.display_message('Контакт успешно обновлен', 'green')

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
            ConsoleUI.display_menu()
            choice = input('Выберите действие: ')

            if choice == '1':
                ConsoleUI.clear_console()
                ConsoleUI.display_contacts(phone_book.contacts)

            elif choice == '2':
                ConsoleUI.clear_console()
                new_contact = ConsoleUI.input_data()
                contact = Contact(**new_contact)
                phone_book.add_contact(contact)
                ConsoleUI.display_message('Новый контакт успешно добавлен', 'green')

            elif choice == '3':
                ConsoleUI.edit_contact(phone_book)

            elif choice == '4':
                contact_data = ConsoleUI.input_data(mode='filter')
                indices = phone_book.find_contacts(contact_data)
                message = ('По заданным критериям найдены контакты: ', 'green') if indices \
                    else ('По заданным критериям ничего не найдено: ', 'yellow')
                ConsoleUI.display_message(*message)

                if indices:
                    ConsoleUI.display_contacts(phone_book.contacts, indices)

            elif choice == '0':
                print('Выход...')
                return 0

            else:
                ConsoleUI.display_message(
                    'Некорректный выбор. Пожалуйста, выберите действие из меню.',
                    'red')
