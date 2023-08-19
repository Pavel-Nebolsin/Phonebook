from contact import Contact


class ConsoleUI:
    @staticmethod
    def input_contact_data():
        print("Введите данные для нового контакта:")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        middle_name = input("Отчество: ")
        organization = input("Организация: ")
        work_phone = input("Телефон (рабочий): ")
        personal_phone = input("Телефон (личный): ")

        new_contact = {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "organization": organization,
            "work_phone": work_phone,
            "personal_phone": personal_phone
        }

        return new_contact

    @staticmethod
    def input_search_criteria():

        pass

    @staticmethod
    def display_contacts(contacts):
        for contact in contacts:
            print(contact)

    @staticmethod
    def display_search_results(results):
        pass

    @staticmethod
    def display_message(message):
        pass

    @staticmethod
    def display_menu():
        print("Меню:")
        print("1. Добавить контакт")
        print("2. Вывести все контакты")
        print("0. Выйти")

        # Добавьте другие пункты меню по мере необходимости

    @staticmethod
    def run(phone_book):
        while True:
            ConsoleUI.display_menu()
            choice = input("Выберите действие: ")

            if choice == '1':
                new_contact = ConsoleUI.input_contact_data()
                contact = Contact(**new_contact)
                phone_book.add_contact(contact)

            elif choice == '2':
                ConsoleUI.display_contacts(phone_book.contacts)

            elif choice == '0':
                print("Выход...")
                return 0

            else:
                print("Некорректный выбор. Пожалуйста, выберите действие из меню.")

            print("-"*30)

