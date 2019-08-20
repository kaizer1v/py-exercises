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


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
























