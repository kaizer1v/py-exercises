from game import Game

line_sep = '--'
move_sep = ','
coins = {
    'black': 9,
    'red': 1,
    'striker': 1
}

# read inputs
f = open('inputs.txt')
moves = f.read().replace('\n', '').split(line_sep)
f.close()

# create a game with some settings and 2 players
g = Game(players=2, coins=coins)

# play, until the game finishes
for m in moves:
    if not g.is_finish():
        g.play(m)
        # print(g.get_board())
        # print('-'.join(map(str, g.get_points())))

print('Player {} won the game. Final Score:'.format(
    g.get_winner()
), '-'.join(map(str, g.get_points())))
