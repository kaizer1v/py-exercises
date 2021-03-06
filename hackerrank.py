---
title: Redesigning My Electricity Bill
categories: [design]
tags: [design, ui-design]
---

Here's what my electricity looks like. Infact, all of Bangalore's electricity might look the same. Although it provides all the required information that I need to know from a bill, I thought of making it a little more efficient considering the following factors

* Information hierarchy
* Paper print efficiency
* Discarding unwanted information
* Language


## What does one want to know from their electricity bill?

1. The amount due
2. The due date
3. The period billed for
4. Breakdown for the total amount
5. Payment


## Who actually uses the bill printout?

* The person who sorts the bills and allots the bills based on the locality
* The delivery person who actually delivers the printout
* The third party person who reads the address
* The resident

Let's look at how the bill flows; right from where it is printed, to the residen'ts location.

The goal of each of these users are a little different, let's see what their goals are.

### User 1 - The person who sorts the bills

In order to sort the bills fast, assuming that they do it manually, would be interested in the locality of the address or the connection number.


### User 2 - Delivery Man

The delivery person mainly focuses on the delivery of the bill at the right address. Also, since these personnels are regular delivery personnels, their **addresses** and routes are already known to them. They group the bills based on the apartment names and deliver in bulk.


### User 3 - Middle Man

These personnels are usually like apartment security guards, neighbours or who are in direct contact with the delivery personnels and collect the bill from them in bulk. They then destribute and deliver it to the door step of the resident


### User 4 - Resident

The final user would be the resident who is mostly concerned with information concerned with the amount due and the due date. They also sometimes refer to the account number when dealing with either the website or customer care.


## Current Bill

This is what the current bill looks like.

<figure class="row justify-content-center figure text-center">
  <img src="/assets/images/bill_original.png" class="border figure-img img-fluid rounded col-md-5" alt="electricity bill">
</figure>

<h2 class="h2">Proposed Redesign</h2>

Considering the above factors and a bit of research, here is the proposed redesign of the electricity bill.

<figure class="row justify-content-center figure text-center">
  <img src="/assets/images/bill_redesign_full.png" class="border figure-img img-fluid rounded col-md-3" alt="electricity bill redesigned">
</figure>

<h3 class="h3">Minimal Version</h3>

**What the minimal bill redesign addresses**

* Promotes digital payment option with PayTM or BEC app
* Reduces paper size
* Removal of secondary information like kilo-watt rates and total amount breakdown
* Changes hierarchy of information from usage point of view for all users involved (top to bottom)

<figure class="row justify-content-center figure text-center">
  <img src="/assets/images/bill_redesign_minimal.png" class="border figure-img img-fluid rounded col-md-3" alt="electricity bill redesigned minimal">
</figure>

Would love to have comments, critic or suggestions on this proposal.







                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        s`

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
    elif 30 < m <= 59:
        if h + 1 > 12:
            h = (h - 12)
        if m == 45:
            to_return = 'quarter to ' + getWord(h + 1)
        elif m == 1:
            to_return = getWord(60 - m) + ' minute to ' + getWord(h + 1)
        else:
            to_return = getWord(60 - m) + ' minutes to ' + getWord(h + 1)
    elif 1 <= m < 30:
        if m == 15:
            to_return = 'quarter past ' + getWord(h)
        elif m == 1:
            to_return = getWord(m) + ' minute past ' + getWord(h)
        else:
            to_return = getWord(m) + ' minutes past ' + getWord(h)
    elif m == 30:
        to_return = 'half past ' + getWord(h)
    return to_return

# print(timeInWords(5, 30))
# print(timeInWords(5, 20))
# print(timeInWords(3, 00))
# print(timeInWords(3, 15))
# print(timeInWords(12, 45))
# print(timeInWords(12, 29))
# print(timeInWords(12, 59))







    


'''
algo to find the closest pair that (add, sub, product ...) to
some number

here the sum shouldn't be greater than 60
'''
import sys
def getMoneySpent(keyboards, drives, b):
    # k = 0
    # d = len(drives) - 1
    total = -2

    for k in keyboards:
        for d in drives:
            if (k + d) > total and (k + d) <= b:
                total = (k + d)

    if total == -2:
        return -1
    return total


# print(getMoneySpent([3, 1], [5, 2, 8], 10))
# print(getMoneySpent([5], [0], 5))






'''
generate a dictionary holding the number occurances
for each integer
'''
def countingSort(arr):
    if max(arr) <= len(arr):
        results = [0 for i in range(len(arr))]
        for val in arr:
            results[val] += 1

        return results

# arr = ['63', '25', '73', '1', '98', '73', '56', '84', '86', '57', '16', '83', '8', '25', '81', '56', '9', '53', '98', '67', '99', '12', '83', '89', '80', '91', '39', '86', '76', '85', '74', '39', '25', '90', '59', '10', '94', '32', '44', '3', '89', '30', '27', '79', '46', '96', '27', '32', '18', '21', '92', '69', '81', '40', '40', '34', '68', '78', '24', '87', '42', '69', '23', '41', '78', '22', '6', '90', '99', '89', '50', '30', '20', '1', '43', '3', '70', '95', '33', '46', '44', '9', '69', '48', '33', '60', '65', '16', '82', '67', '61', '32', '21', '79', '75', '75', '13', '87', '70', '33']
# mapped_arr = list(map(lambda x: int(x), arr))

# print(countingSort([]))
# print(countingSort([1, 1]))





'''
find the smallest absolute difference between elements of an array
'''
def closestNumbers(arr):
    # s_arr = sorted(arr)
    l = 0
    r = len(arr) - 1
    diff = sys.maxsize
    to_return = []

    while l < r:
        # If this pair is closer to diff than  
        # the previously found closest, 
        # then update res_l, res_r and diff 
        if abs(arr[l] - arr[r]) < diff:
            diff = abs(arr[l] - arr[r])
            to_return = []
            to_return.extend([arr[l], arr[r]])
            l = l + 1

        if abs(arr[l] - arr[r]) > diff: 
            r = r - 1
        # elif abs(arr[l] - arr[r]) < diff:
        #     l = l + 1
        else:
            to_return.extend([arr[l], arr[r]])
            l = l + 1
            # r = r - 1

        print('left={:d}, right={:d} & diff={:d}'.format(arr[l], arr[r], diff))

    return to_return


# print(closestNumbers([1, 2, 3, 4, 5]))
# print(closestNumbers([-70, -64, -39, -36, -35, -20, 30, 266, 624, 737]))







'''
given two arrays, find the missing items from the second array <brr> within the
first array <arr>

brr = original array without the missing items
arr = array with missing items
'''
def missingNumbers(arr, brr):
    to_return = []
    b_len = len(brr)
    a_len = len(arr)
    i, j = 0, 0

    if arr == brr:
        return []

    if a_len < b_len:
        while j < a_len and i < b_len:
            if brr[i] != arr[j]:
                to_return.append(brr[i])
                i += 1
            else:
                if i == b_len:
                    j += 1
                elif j == a_len:
                    i += 1
                else:
                    i += 1
                    j += 1

    elif a_len > b_len:
        # the input is wrong
        return []

    if i < b_len:
        to_return += brr[i:]

    return sorted(len(set(to_return)))

# print(missingNumbers(
#     [1, 2, 4, 5, 8, 1, 10],                # j
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10]     # i
# ))

# print(missingNumbers(
#     [11, 4, 11, 7, 13, 4, 12, 11, 10, 14],                            # j
#     [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]            # i
# ))

# print(missingNumbers(
#     [203, 204, 205, 206, 207, 208, 203, 204, 205, 206],                 # j
#     [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]   # i
# ))






'''
given a set multiple lists, find the intersecting path
between `path` and `other` and output the intersecting
path only

eg: path = [1, 2, 3, 4, 5, 6]
& other = [3, 4, 5, 7, 9]

output should be [3, 4, 5]

Asymtotic time O(p * o)
'''
def longestIntersection(p, o):
    i = 0
    j = 0
    temp = []
    intersection = []

    while p[i] != o[j]:
        if p[i] == o[j]:
            hold_i = i
            hold_j = j
            temp = []
            while p[hold_i] != o[hold_j]:
                temp.append(p[hold_i])
                hold_i += 1
                hold_j += 1

            if len(temp) > len(intersection):
                intersection = temp
                temp = []
                i += 1
        j += 1



print(longestIntersection(
    [5, 7, 9, 7, 6, 2, 4, 8],
    [1, 3, 7, 9, 7, 4, 8]
))
