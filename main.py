def add_in_pb(info):
    with open("phone_book.txt", "a") as file:
        file.write('\n'+'|'.join(info))


def get_from_pb():
    with open("phone_book.txt", "r") as file:
        return file.read().splitlines()


def find_in_pb(str):
    with open("phone_book.txt", "r") as file:
        result = []
        for line in file:
            if str in line:
                result.append(line.rstrip())
        return result


def delete_from_pb(index):
    with open("phone_book.txt", "r") as temp:
        pb = temp.readlines()
    pb.pop(index-1)
    with open("phone_book.txt", "w") as file:
        file.writelines(pb)


def replace_in_pb(index, str):
    with open("phone_book.txt", "r") as temp:
        pb = temp.readlines()
    pb[index-1] = str + '\n'
    with open("phone_book.txt", "w") as file:
        file.writelines(pb)




# add_in_pb(['Викторов', 'Виктор', 'Викторович', 'Виктория', '99-00-33', '+7-342-574-12-44'])
# print(get_from_pb())
# print(find_in_pb('99'))
# delete_from_pb(3)
# replace_in_pb(3, 'Дмитрий|Дмитриевич|Дмитров|Фейсбук|32-24-76|+7-902-757-86-53')
