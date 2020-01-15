# Make every even letter uppercase
def myfunc(input_str):
    str_arr = list(input_str)
    str_arr[0] = str_arr[0].lower()

    for i, char in enumerate(str_arr):
        if (i + 1) % 2 == 0:
            str_arr[i] = char.upper()

    return ''.join(str_arr)

print(myfunc('Anthropomorphism'))

# LESSER OF TWO EVENS:
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return num1 if num1 - num2 < 0 else num2
    return num1 if num1 - num2 > 0 else num2

print(lesser_of_two_evens(2, 4)) # 2
print(lesser_of_two_evens(5, 3)) # 5

# ANIMAL CRACKERS:
# Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(word):
    word_arr = word.split()

    if len(word_arr) > 2:
        return None
    
    return word_arr[0][0].lower() == word_arr[1][0].lower()

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY:
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(num1, num2):
    return num1 == 20 or num2 == 20 or num1 + num2 == 20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(word):
    return word.capitalize()[:3] + word[3:].capitalize()

print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoda(sentence):
    sentence_arr = sentence.split()
    sentence_arr.reverse()
    return ' '.join(sentence_arr)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
def almost_there(num):
    return abs(100 - num) <= 10 or abs(200 - num) <= 10

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def has_33(int_list):
    if 3 in int_list:
        return int_list[int_list.index(3) + 1] == 3 or (int_list[int_list.index(3) - 1] == 3 and int_list.index(3) != 0)
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# BLACKJACK:
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(*args):
    THRESHOLD = 21
    total = sum(args) - 10 if 11 in args else sum(args)
    return total if total <= THRESHOLD else 'BUST!' 

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

# SUMMER OF '69:
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
    total = 0
    arr_to_sum = arr

    if 6 in arr and 9 in arr:
        arr_to_sum = arr[0:arr.index(6)] + arr[arr.index(9) + 1:]
    
    total = sum(arr_to_sum)

    return total

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# SPY GAME:
# Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(num_list):
    if 7 in num_list and num_list.count(0) == 2:
        new_list = [str(num) for num in num_list if num == 0 or num == 7]
        return ''.join(new_list) == '007'

    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


# COUNT PRIMES:
# Write a function that returns the number of prime numbers that exist up to and including a given number
# By convention, 0 and 1 are not prime.
# count_primes(100) --> 25
def count_primes(num):
    if num < 2:
        return 0

    prime_numbers = [2]
    count = 3

    while count <= num:
        for y in range(3, count, 2):
            if num % y == 0:
                count += 2
                break
        else:
            prime_numbers.append(count)
            count += 2

    return len(prime_numbers)
