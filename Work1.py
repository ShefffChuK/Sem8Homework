# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def show_data(filename):
    print("\n ФИО, Телефон, Описание")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        description_user = input("Введите описание: ")
        data.write(f"{num},  {fio}, {phone_number}, {description_user}\n")
        print(f"Добавлена запись : {num}, {fio}, {phone_number}, {description_user}\n")

def edit_data(filename):
    print("\nФИО, Телефон, Описание")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" , ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    description_user = input("Введите описание: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} , {fio}, {phone},  {description_user}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines} - изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def delete_data(filename):
    print("\n ФИО, Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    my_choice = -1
    file_tel = "phonebook.csv"

    
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Добавление данных")
        print("3 - Изменение данных")
        print("4 - Удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("Удачи!")

if __name__ == "__main__":
    main()
