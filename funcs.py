from config import phone_book

Record = tuple[str, str, str, str, str, str]


def to_record(row: str) -> Record:
    """
    Функция преобразования строки в переменную типа Record.
    :param row: Строка с информацией.
    :return: Информация в виде переменной типа Record.
    """
    info = row.split('|' if '|' in row else ',')
    return info[0], info[1], info[2], info[3], info[4], info[5]


def to_row(record: Record) -> str:
    """
    Функция преобразования переменной типа Record в строку.
    :param record: Информация в виде переменной типа Record.
    :return: Строка с информацией.
    """
    return '|'.join(record)


def add(info: Record):
    """
    Функция добавления новой записи в конец базы данных.
    :param info: Информация в виде переменной типа Record.
    """
    with open(phone_book, "a") as file:
        file.write('\n'+to_row(info))


def get() -> list[Record]:
    """
    Функция получения всех записей из базы данных.
    :return: Информация в виде списка переменных типа Record.
    """
    with open(phone_book, "r") as file:
        return [to_record(s) for s in file.read().splitlines()]


def find(phrase: str) -> list[Record]:
    """
    Функция поиска в базе данных по фразе (строка или число).
    :param phrase: Фраза для поиска.
    :return: Результат поиска в виде списка переменных типа Record.
    """
    with open(phone_book, "r") as file:
        return [to_record(s) for s in file.read().splitlines() if phrase in s]


def replace(index: int, info: Record):
    """
    Функция замены информации в конкретной строке базы данных.
    :param index: Индекс записи, которую нужно изменить.
    :param info: Строка, на которую нужно заменить информацию в базе данных.
    """
    with open(phone_book, "r") as file:
        pb = file.readlines()
    pb[index-1] = to_row(info) + '\n'
    with open(phone_book, "w") as file:
        file.writelines(pb)
