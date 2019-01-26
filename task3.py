documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "100099", "name": None}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

print(documents)

print(directories)


##########################################################
#####   ЗАДАЧА   № 1      ###############################
##########################################################

# поиск документов по номеру
def search_name_for_number_func(document):
    doc_number = str(input('Введите номер документа: '))
    result = 'Совпадений не найдено'
    n = 1
    for row in document:
        if row["number"] == doc_number:
            result = row["name"]
            print('Владелец документа: ', result)
            break
        else:
            continue
    return result


# name_user = search_name_for_number_func(documents)
# print('Владелец документа: ', name_user)


# список документов
def list_documents(document):
    print()
    print('Список документов: ')
    for row in document:
        # print(row["type"],row["number"],' ',row["name"],'"',sep = '"')
        print("{} {}{}{}  {}{}{}".format(row["type"], '"', row["number"], '"', '"', row["name"], '"'))


list_documents(documents)


# поиск документа на полке
def shelf_document(directorie):
    doc_number = str(input('Введите номер документа: '))
    result = 'Документ не найден'
    for key, val in directorie.items():
        if doc_number in val:
            result = key
            print('Документ находиться на полке № ', result)
            break
        else:
            continue
    return result


# shelf = shelf_document(directories)


# добавление документа
def add_document(directorie, document):
    doc_number = str(input('Введите номер добавляемого документа: '))
    doc_owner = str(input('Введите владельца документа: '))
    doc_type = str(input('Введите тип документа: '))
    doc_number_shelf = str(input('Введите номер полки: '))

    for key, val in directorie.items():
        priznak = 0
        if key == doc_number_shelf:
            directorie[key].append(doc_number)
            priznak = 1
        else:
            priznak = 0
    if priznak == 1:
        document.append({
            "type": doc_type,
            "number": doc_number,
            "name": doc_owner,
        })
        print('Документ успешно добавлен')
    else:
        print('Документ не добавлен. Неверно указана полка. Нужно добавить номер полки в словарь.')
    print(document)
    print(directorie)


# add_document(directories, documents)


##########################################################
#####   ЗАДАЧА   № 2      ###############################
##########################################################
# добавление полки
def add_shelf(directorie):
    doc_number_shelf = str(input('Введите номер добавляемой полки: '))
    if doc_number_shelf in (directorie.keys()):
        print('Полка существует')

    else:
        directorie[doc_number_shelf] = []
        print(directorie)
    return doc_number_shelf


# add_shelf(directories)


# удаление документа
def delete_document(directorie, document):
    doc_number = str(input('Введите для удаления номер документа : '))
    i = -1
    find_doc = 0
    for d in document:
        i += 1
        if d['number'] == doc_number:
            document.pop(i)
            find_doc = 1
    if find_doc == 1:
        for key, val in directorie.items():
            if doc_number in val:
                n = -1
                for row in val:
                    n += 1
                    if row == doc_number:
                        val.remove(row)
    else:
        print('Документ для удаления не найден. Операция не выполнена')
    print(document)
    print(directorie)


# delete_document(directories, documents)


# Перемещение документа
def moving_document(directorie):
    doc_number = str(input("Введите номер перемещаемого документа: "))
    doc_number_shelf = str(input("Введите новый номер полки: "))
    if doc_number_shelf in (directorie.keys()):
        for key, val in directorie.items():
            if doc_number in val:
                n = -1
                for row in val:
                    n += 1
                    if row == doc_number:
                        val.remove(row)
        directorie[doc_number_shelf].append(doc_number)
        print('Документ успешно перемещен')
    else:
        print('Документ переместить невозможно, неправильно указана полка назначения')
    print(directorie)


# moving_document(directorie)


# list name documents

def list_name(document):
    try:
        print("Владельцы:")

        for d in document:
            if d["name"] != None:
                print(d["name"])
            else:
                str = d["number"]
                raise KeyError
    except KeyError:
       print(' У документа {} нет владельца'.format(str))
       print("Исключение перехвачено")


# Функция пользовательского ввода операций

def user_input_action(directories, documents):
    user_action = 'p'
    while user_action != 'q':
        print('Введите команды для выполнения действий')
        print('p - (people) –  вывод имени человека по номеру документа,')
        print('l - (list) - список всех документов,')
        print('s – (shelf) – вывoдит номер полки по номеру документа,')
        print('a – (add )– добавление нового документа в каталог и в перечень полок, спросив его номер, тип, имя,')
        print('d – (delete) – удаляет документ из каталога и из перечня полок, спросив номер документа,')
        print('m – (move) – перемещение  документа на целевую полку,')
        print('as – (add shelf) – добавление новой полки в перечень')
        print('n - Список всех владельцев документов')
        print('q - (quit) - выход из программы')
        user_action = str(input('Ваш выбор:'))
        print(directories)
        print(documents)
        if user_action == 'p':
            search_name_for_number_func(documents)
            print('=============================================')
            print('вывод имени человека по номеру документа')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'l':
            list_documents(documents)
            print('=============================================')
            print('список всех документов')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 's':
            shelf_document(directories)
            print('=============================================')
            print('Поиск документа на полке')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'a':
            add_document(directories, documents)
            print('=============================================')
            print('Добавление документа')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'd':
            delete_document(directories, documents)
            print('=============================================')
            print('Удаление документа')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'm':
            moving_document(directories)
            print('=============================================')
            print('Перемещение документа')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'as':
            add_shelf(directories)
            print('=============================================')
            print('Добавление полки')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'n':
            list_name(documents)
            print('=============================================')
            print('Список всех владельцев документов')
            print('=============================================')
            input('Press any key to continue:')
        elif user_action == 'q':
            print('=============================================')
            print('Завершение программы')
            print('=============================================')

        else:
            print('Введена неправильная команда, попробуйте еще раз')
    print('Работа программы завершена')


user_input_action(directories, documents)
