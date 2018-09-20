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
        'white': 9,
        'black': 9,
        'red': 1,
        'striker': 1
    })

    # play moves <m>
    for m in t.split(line_sep):
        g.play(m)

    result = g.get_result()
    final_score = ' <-> '.join(map(str, g.get_points()))
    # print(result, final_score)

    # print the result
    if result == 'draw':
        print('Game ended as a draw. Final Score: {}'.format(final_score))
    elif type(result) is int:
        print('Player {} won the game. Final Score: {}'.format(
            g.get_result(),
            final_score
        ))
    print('---------------------')
