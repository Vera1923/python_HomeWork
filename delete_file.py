from print_file import print_data

def delete_data():
    with open('data_1.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print_data()
        delete_row = int(input("Введите номер строки, которую нужно удалить: "))
        if 1 <= delete_row <= len(lines):
            line_copy = lines[delete_row - 1]
            with open('data_1.txt', 'w', encoding='utf-8') as file:
                file.writelines(line_copy)
                print(f'Строка {delete_row} успешно удалена')
        else:
            print(f'Недопустимый номер строки. В файле  всего {len(lines)} строк.')
            
   


        