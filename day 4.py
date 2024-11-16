# вводные данные
"""text = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')"""

text = [l.strip() for l in open('day 4 input.txt').readlines()]
total_points = 0

for row in text:
    row = row.split(':')[1].split('|')
    win_num, my_num = row[0].split(), row[1].split()
    counter = 0
    counter = sum(1 for num in my_num if num in win_num)
    if counter > 0:
        total_points += 2 ** (counter - 1)
print(total_points)