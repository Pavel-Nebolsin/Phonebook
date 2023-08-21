import os
import sys


def text_color(message: str, color: str | None = None) -> str:
    """
    Возвращает строку, окрашенную в указанный цвет.

    :param message: Текст для окрашивания.
    :param color: Цвет текста. Может быть 'red', 'green', 'yellow', 'blue' или None.
    :return: Окрашенная строка.
    """
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


def clear_console() -> None:
    """
    Очищает консольный вывод.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def move_cursor_up(lines: int = 1) -> None:
    """
    Перемещает курсор на указанное количество строк вверх.

    :param lines: Количество строк для перемещения.
    """
    for _ in range(lines):
        sys.stdout.write('\033[F\033[K')
        sys.stdout.flush()
