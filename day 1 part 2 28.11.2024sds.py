words_to_digits = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
                }
def find_digits(string):
    all_digits = {}
    for key, value in words_to_digits.items():
        number_index = string.find(key)
        while number_index != -1:
            all_digits[number_index] = value
            number_index = string.find(key, number_index + 1)
    first_digit = all_digits[min(all_digits)]
    last_digit = all_digits[max(all_digits)]
    return int(str(first_digit) + str(last_digit))

with open(r'C:\pt\github\Advent_of_Code_2023\day 1 input.txt') as file:
    total = 0
    text = file.readlines()
    for string in text:
        total += find_digits(string.strip())
    print(total)