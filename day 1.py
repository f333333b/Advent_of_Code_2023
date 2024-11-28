text = [l.strip() for l in open('day 1 input.txt').readlines()]
total_numbers = 0
for row in text:
    numbers_in_row = [char for char in row if char.isdigit()] # создаём список всех чисел в строке
    number = numbers_in_row[0] + numbers_in_row[-1] # создаём двухзначное число из строки
    total_numbers += int(number) # добавляем число из строки в общую сумму
print(total_numbers)

#TODO