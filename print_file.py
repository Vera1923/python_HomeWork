
def print_data():
    with open('data_1.txt', 'r', encoding='utf-8') as f:
        data_1 = f.readlines()
        print(*data_1)
    