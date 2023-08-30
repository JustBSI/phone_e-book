import funcs
import click
import math
from config import rows_per_page


@click.group()
def main():
    """Функция для группировки функций."""
    ...


def show(rows: list, page: int):
    """
    Функция, постранично выводящая информацию в консоль.
    :param rows: Список строк для вывода.
    :param page: Номер страницы.
    """
    click.clear()
    data = rows[(page-1) * rows_per_page: page * rows_per_page]
    headers = ('ID', 'Фамилия', 'Имя', 'Отчество', 'Орг.', 'Р.номер', 'Личный номер')
    max_lens = (len(str(page * rows_per_page)), *[max(len(elem[i]) for elem in data) for i in range(len(data[0]))])

    click.secho(' │ '.join(f'{headers[i]:^{max_lens[i]}}' for i in range(7)) +
                '\n' + '─' * (sum(max_lens)+18), bold=True)

    for index, elem in enumerate(data):
        indexes = f'{((page-1) * rows_per_page) + index+1:<{max_lens[0]}} │ '
        info = (f'{elem[i]:{max_lens[i+1]}}' for i in range(len(elem)))
        click.echo(indexes + ' │ '.join(info))

    click.secho(f"{f'Страница {page} из {math.ceil((len(rows))/rows_per_page)}':^{sum(max_lens)+18}}",
                italic=True, bold=True)


@main.command()
@click.option('--page', type=click.IntRange(1, math.ceil(len(funcs.get())/rows_per_page), clamp=True), default=1)
def view(page: int):
    """
    Функция постраничного вывода всех записей базы данных в консоль.
    :param page: Номер страницы.
    """
    show(funcs.get(), page)


@main.command()
@click.option('--phrase', type=str, required=True)
@click.option('--page', type=int, default=1)
def find(phrase: str, page: int):
    """
    Функция поиска по фразе в базе данных и постраничного вывода результата поиска в консоль.
    :param phrase: Фраза для поиска.
    :param page: Номер страницы.
    """
    click.clear()
    result = funcs.find(phrase)
    if len(result) != 0:
        if 1 <= page <= math.ceil(len(phrase)/rows_per_page):
            show(result, page)
        else:
            click.secho('Нет страницы с таким номером!', bold=True, fg='red')
    else:
        click.secho('Ничего не найдено!', bold=True, fg='red')


@main.command()
@click.argument('info', type=str, required=True)
def add(info: str):
    """
    Функция добавления записи в базу данных.
    :param info: Строка с информацией, добавляемая в базу данных, в формате:
                'Иванов,Иван,Иванович,Яндекс,12-34-56,+7-999-123-45-67'.
                Одинарные кавычки и запятые (без пробелов) обязательны.
    """
    click.clear()
    if info.count(',') == 5:
        funcs.add(funcs.to_record(info))
        click.secho('Добавлено!', bold=True, fg='green')
    else:
        click.secho('Некорректная строка!', bold=True, fg='red')


@main.command()
@click.argument('index', type=int, required=True)
@click.argument('info', type=str, required=True)
def edit(index: int, info: str):
    """
    Функция изменения записи в базе данных по индексу.
    :param index: Индекс записи, которую нужно изменить.
    :param info: Строка, на которую нужно заменить информацию в базе данных.
    """
    click.clear()
    if info.count(',') == 5:
        if 1 <= index <= len(funcs.get()):
            funcs.replace(index, funcs.to_record(info))
            click.secho('Изменено!', bold=True, fg='green')
        else:
            click.secho('Нет записи с таким индексом!', bold=True, fg='red')
    else:
        click.secho('Некорректная строка!', bold=True, fg='red')
