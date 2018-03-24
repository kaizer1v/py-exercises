# Paste your code into this box

print('Please think of a number between 0 and 100! ')

low = 0
high = 100
guess = (low + high) / 2
lhc = ''
while lhc != 'c':
    lhc = input(
        'Is your number %d? {} ? \nEnter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.'.format(guess))
    if lhc == 'l':
        low = guess
    elif lhc == 'h':
        high = guess
    elif lhc == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
    guess = (low + high) // 2

print('Game over. Your secret number was {}'.format(guess))
