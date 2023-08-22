import funcs
import click


@click.group()
def main():
    ...


@main.command()
def view():
    click.clear()
    pb = funcs.get()
    max_lens = (len(str(len(pb))), *[max(len(elem[i]) for elem in pb) for i in range(len(pb[0]))])
    headers = ('ID', 'Фамилия', 'Имя', 'Отчество', 'Орг.', 'Р.номер', 'Личный номер')

    click.echo(' | '.join(f'{headers[i]:^{max_lens[i]}}' for i in range(7)) + '\n' + '–' * (sum(max_lens)+18))

    for index, elem in enumerate(pb):
        indexes = f'{index+1:<{max_lens[0]}} | '
        info = (f'{elem[i]:{max_lens[i+1]}}' for i in range(len(elem)))
        click.echo(indexes + ' | '.join(info))


if __name__ == '__main__':
    main()
