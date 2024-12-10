def check_game(game):
    grabs = game.strip().partition(':')[2][1:].split('; ')
    colors = {'red': 0, 'green': 0, 'blue': 0}
    for one_grab in grabs:
        one_grab = [i.strip() for i in one_grab.split(',')]
        for i in range(len(one_grab)):
            color = one_grab[i].split()
            if int(color[0]) > colors[color[1]]:
                 colors[color[1]] = int(color[0])
    return colors['red'] * colors['green'] * colors['blue']

with open(r"day 2 input.txt") as file:
    text = file.readlines()
    print(sum(check_game(game) for game in text))