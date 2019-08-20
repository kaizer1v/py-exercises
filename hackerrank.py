'''
given a list of movements
D - Down
U - Up 
'''
def countingValleys(n, s):
    level = 0
    valleys = 0
    mountains = 0
    for step in s:
        if step == 'D':
            level = level - 1
            if level == 0:
                moutains = mountains + 1
        else:   # step == 'U'
            level = level + 1
            if level == 0:
                valleys = valleys + 1
    return valleys

# countingValleys(8, 'UDDDUDUU')        # 1






'''
given a list of integers. Return the most commonly occurring integer.
If there are more then one integer with the same repitions, return the one with
the smaller value
'''
def migratoryBirds(arr):
    d = {}
    for bird in arr:
        if bird in d:
            d[bird] += 1
        else:
            d[bird] = 1

    mode = sorted(d.items(), key=lambda x: (x[1], -x[0]), reverse=True)
    return mode[0][0]

# print(migratoryBirds([1, 4, 4, 5, 3, 4]))  # 4
# print(migratoryBirds([1, 2, 4, 2, 3, 4]))  # 4





'''
Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

super_digit(9875)   9+8+7+5 = 29 
super_digit(29)     2 + 9 = 11
super_digit(11)     1 + 1 = 2
super_digit(2)      = 2  
'''
def superDigit(n, k):
    if k <= 0:
        k = 1
    p = str(n) * k

    def compute(num):
        # sum of all digits until it's a single digit
        if num < 10:
            return num
        print('>>>>', (num % 10), ' + ', num // 10)
        return (num % 10) + compute(num // 10)

    total = compute(int(p))
    while total > 10:
        total = compute(total)
    return total
    


# print(superDigit(12341, 1))
# print(superDigit(148, 3))
# print(superDigit(1234191, 1))
# print(superDigit(9875, 4))
# print(superDigit(4757362, 3))





'''
you share an advert with x people the first day. Next day, half of x i.e. x/2
share it with three people. This happens continuously. You need to find out
the number of people the advert reached on `n`th day.
'''
def viralAdvertising(n):
    shared = 5
    total = 0
    for day in range(0, n):
        liked = shared // 2
        total += liked
        shared = liked * 3
    return total

# print(viralAdvertising(5))





'''
count the number of maximum values in the list
'''
def birthdayCakeCandles(ar):
    if len(ar) == 0:
        return 0
    if len(ar) == 1:
        return 1
    tallest = ar[0]
    count = 1
    for candle in ar:
        print(candle, tallest)
        if candle > tallest:
            tallest = candle
            count = count + 1
    return count

# print('1 ->', birthdayCakeCandles([1, 3, 2, 1, 3]))
# print('2 ->', birthdayCakeCandles([]))
# print('3 ->', birthdayCakeCandles([5]))
# print('4 ->', birthdayCakeCandles([1, 1, 1, 1, 1]))





'''
given a list of integers and a value `k`, return the difference
between the max - k
'''
def hurdleRace(k, height):
    highest = max(height)
    if k >= highest:
        return 0
    return abs(highest - k)


# print(hurdleRace(4, [1, 6, 3, 5, 2]))          # 2
# print(hurdleRace(7, [2, 5, 4, 5, 2]))          # 0





'''
Divisible sum pairs

where i < j & 
such that ar[i] & ar[j] is divisible k

return the number of such pairs
'''
def divisibleSumPairs(n, k, ar):
    # sorted_ar = sorted(ar)
    if len(ar) < 1:
        return 0

    count = 0
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0 and i != j:
                temp_arr.append((ar[i], ar[j]))
                count += 1
    return count


# print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))





'''
return the factorial of a number
'''
def extraLongFactorials(n):
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    print(factorial(n))

# extraLongFactorials(1)
# extraLongFactorials(5)
# extraLongFactorials(25)






'''
given a sentence like
    `if man was meant to stay on the ground god would have given us roots`

do the following
1. remove the spaces 
2. compute the length (= 56)
3. take square root of the length (between 7 & 8)
4. arrange the sentence in 7 rows & 8 columns 
like

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots

'''
import math
def encryption(s):
    stripped = s.replace(' ', '')
    length = len(stripped)
    sqrt = math.sqrt(length)
    rounded = round(sqrt)
    to_print = ''
    if sqrt == rounded:
        # perfect square
        rows, cols = sqrt, sqrt
    else:
        rows = rounded
        cols = rounded - 1

    for i in range(length):
        to_print += stripped[i]
        if i == cols:
            to_print += '\n'

    return to_print

'''
chi
llo
ut
'''
# print(encryption('clu hlt io'))






'''
given a time, convert it to words, for example

5:00    - five 'o' clock
5:45    - quarter to six
5:15    - quarter past five
5:30    - half past five

basically for
- minutes = 0, use `o` clock
- 1 <= minutes <= 30 use `past`
- minutes > 30 use `to`
'''
def timeInWords(h, m):
    def getWord(n):
        words = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'quarter',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            21: 'twenty one',
            22: 'twenty two',
            23: 'twenty three',
            24: 'twenty four',
            25: 'twenty five',
            26: 'twenty six',
            27: 'twenty seven',
            28: 'twenty eight',
            29: 'twenty nine',
            30: 'half'
        }
        return words[n]
    if m == 0:
        to_return = getWord(h) + ' o\' clock'
    elif m > 30 and m <= 59:
        if h + 1 > 12:
            h = (h - 12)
        if m == 45:
            to_return = 'quarter to ' + getWord(h + 1)
        elif m == 1:
            to_return = getWord(60 - m) + ' minute to ' + getWord(h + 1)
        else:
            to_return = getWord(60 - m) + ' minutes to ' + getWord(h + 1)
    elif m >= 1 and m < 30:
        if m == 15:
            to_return = 'quarter past ' + getWord(h)
        elif m == 1:
            to_return = getWord(m) + ' minute past ' + getWord(h)
        else:
            to_return = getWord(m) + ' minutes past ' + getWord(h)
    elif m == 30:
        to_return = 'half past ' + getWord(h)
    return to_return

print(timeInWords(5, 30))
print(timeInWords(5, 20))
print(timeInWords(3, 00))
print(timeInWords(3, 15))
print(timeInWords(12, 45))
print(timeInWords(12, 29))
print(timeInWords(12, 59))












