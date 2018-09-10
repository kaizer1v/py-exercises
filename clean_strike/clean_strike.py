from game import Game

# constants
p = 2
move_sep = ','
line_sep = '--'
test_sep = '-----'

# read inputs
f = open('inputs.txt')
content = f.read().replace('\n', '')
tests = content.split(test_sep)
f.close()

# run for every test-case
for t in tests:
    # create a game with coins and players
    g = Game(players=p, coins={
        'black': 9,
        'red': 1,
        'striker': 1
    })

    # play moves <m> until the game finishes
    for m in t.split(line_sep):
        if not g.is_game_over():
            g.play(m)

    result = g.get_result()
    final_score = '-'.join(map(str, g.get_points()))

    # print the result
    if result == 'draw':
        print('Game ended as a draw. Final Score: {}'.format(final_score))
    elif type(result) is int:
        print('Player {} the game. Final Score: {}'.format(
            g.get_result(),
            final_score
        ))
    print('---------------------')
