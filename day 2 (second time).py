def check_game(game):
    game_id_num = int(game.strip().partition(':')[0][5::])
    grabs = game.strip().partition(':')[2][1:].split('; ')
    colors = {'red': 12, 'green': 13, 'blue': 14}
    flag = True
    for one_grab in grabs:
        one_grab = [i.strip() for i in one_grab.split(',')]
        for i in range(len(one_grab)):
            dicto = {}
            color = one_grab[i].split()
            dicto[color[1]] = color[0]
            for key in dicto:
                if key in colors and int(dicto[key]) > (colors[key]):
                    flag = False
    if flag:
        #print(game_id_num)
        return game_id_num



"""text = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''"""

#for game in text.split('\n'):
#    check_game(game)

with open(r"C:\pt\github\Advent_of_Code_2023\day 2 input.txt") as file:
    total_ids = 0
    text = file.readlines()
    for game in text:
        if check_game(game):
            total_ids += check_game(game)
    print(total_ids)