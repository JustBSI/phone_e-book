Record = tuple[str, str, str, str, str, str]


def to_record(row: str) -> Record:
    info = row.split('|' if '|' in row else ',')
    return info[0], info[1], info[2], info[3], info[4], info[5]


def to_row(record: Record) -> str:
    return '|'.join(record)


def add(info: Record):
    with open("phone_book.txt", "a") as file:
        file.write('\n'+to_row(info))


def get() -> list[Record]:
    with open("phone_book.txt", "r") as file:
        return [to_record(s) for s in file.read().splitlines()]


def find(phrase: str) -> list[Record]:
    with open("phone_book.txt", "r") as file:
        return [to_record(s) for s in file.read().splitlines() if phrase in s]


def replace(index: int, info: Record):
    with open("phone_book.txt", "r") as file:
        pb = file.readlines()
    pb[index-1] = to_row(info) + '\n'
    with open("phone_book.txt", "w") as file:
        file.writelines(pb)
