from create_data import name_data, surname_data,phone_data,address_data
from print_file import print_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    print_data()
    with open('data_1.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name};{surname};{phone};{address}\n")
    print("Данные успешно записаны!")

