from add_data import input_data
from print_file import print_data
from delete_file import delete_data
from change_file import change_data

def interface():
    print("Добро пожаловать!\nВыберите функцию: \n\n"
          "1 - добавить данные\n"
          "2 - вывод данных\n"
          "3 - изменить данные\n"
          "4 - удалить данные\n")
    command = int(input('Введите число: '))
    while command < 1 or command > 4:
        print("Неправильный ввод")
        command = int(input('Введите число: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
        pass
    elif command == 4:
        delete_data()


