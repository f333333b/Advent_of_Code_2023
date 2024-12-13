# вводные данные
text = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
....*020..'''.split()

# text = [l.strip() for l in open('day 3 input.txt').readlines()]

# переменные
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)] # направления для поиска соседних символов
total = 0 # сумма найденных чисел

# функция проверки на соседей
def check_neighbors(row, col):
    for dr_row, dr_col in directions:
        k_row, k_col = row + dr_row, col + dr_col
        inside_boundary = 0 <= k_row < len(text) and 0 <= k_col < len(text[0])  # условие для проверки на выход за пределы матрицы
        if inside_boundary:
            is_symbol = not (text[k_row][k_col].isdigit() or text[k_row][k_col] == '.') # условие для поиска соседа
            if is_symbol:
                return True
    return False


# функция обработки числа
def process_number(row, col):
    number = ''
    flag_neighbor = False
    if text[row][col] == '0': # проверка на наличие чисел с лидирующим нулём
        while text[row][col].isdigit():
            number += text[row][col]
            col += 1
        print(f'Ошибка! В строке № {row + 1} обнаружено число с лидирующим нулём - {number}')
        return True, 0, col

    else:
        while col < len(text[row]) and text[row][col].isdigit():
            number += text[row][col]
            if check_neighbors(row, col):
                flag_neighbor = True
            col += 1
        return flag_neighbor, int(number), col # возвращаем col для перехода к символу, следующему за последней цифрой

# основной блок
for row in range(len(text)):
    col = 0
    while col < len(text[row]):
        is_valid = not text[row][col].isalpha()  # проверка на то, что символ не является буквенным
        if is_valid:
            if text[row][col].isdigit():
                flag_neighbor, number, col = process_number(row, col)
                if flag_neighbor:
                    total += number
            else:
                col += 1
        else:
            print(f'Ошибка! В строке номер {row + 1} в столбце {col + 1} найдена буква - "{text[row][col]}"')
            quit()
print(total)
