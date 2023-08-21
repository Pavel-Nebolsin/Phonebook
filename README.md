# Телефонный справочник

Консольное приложение для работы с контактами в телефонном справочнике.

## Возможности

- Добавление, редактирование и удаление контактов.
- Поиск контактов по различным критериям.
- Отображение списка контактов с пагинацией.

## Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/Pavel-Nebolsin/Phonebook.git
cd phonebook
```
2. Если хотите заполнить телефонный справчоник, используя API (запустить файл `fill_up_phonebook.py`, инструкция внутри)<br> необходимо установить библиотеку `requests`<br>
если нужно, создайте виртуальное окружение (`python -m venv venv` для Windows, `python3 -m venv venv` для Windows)<br> и далее выполните в консоли:
```
pip install -r requirements.txt
```
или просто
```
pip install requests
```
3. Можно обойтись без установки `requests`, файл с данными `data.json` уже содержит 300 контактов для тестирования.

## Использование
1. Запустите приложение:<br>
Windows: 
```
python main.py
```
Linux: 
```
python3 main.py
```
2. Следуйте инструкциям и подсказкам UI

