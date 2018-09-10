from game import Game

sep = '--'      # seperator
coins = {
    'black': 9,
    'red': 1,
    'striker': 1
}

# read input files
f = open('inputs.txt')
moves = f.read().replace('\n', '').split(sep)

# create a game with some settings and 2 players
g = Game(players=2, coins=coins)

for m in moves:
    p_moves = m.split(',')
    for p, m in enumerate(p_moves):         # turn for every player
        # print(g.show_points(), g.can_have_winner())
        if not g.can_have_winner():
            # play until you have a winner
            g.play(p, int(m))
        else:
            # declare a winner
            print(g.players[p].get_points())

# print('player 0 =', g.players[0].get_points())
# print('player 1 =', g.players[1].get_points())
