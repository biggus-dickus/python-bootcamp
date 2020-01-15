# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
str_list = st.split()

for word in str_list:
    if word[0].lower() == 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10.
for num in range(0, 11):
    if num % 2 == 0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list3 = [num for num in range(1, 50) if num % 3 == 0]
print(list3)

# Go through the string below and if the length of a word is even print "even!"
str2 = 'Print every word in this sentence that has an even number of letters'
for w in str2.split():
    if len(w) % 2 == 0:
        print(w, 'even!')


# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, 'FizzBuzz')
    elif number % 5 == 0:
        print(number, 'Buzz')
    elif number % 3 == 0:
        print(number, 'Fizz')


# Use List Comprehension to create a list of the first letters of every word in the string below:
str3 = 'Create a list of the first letters of every word in this string'
first_letters = [word[0] for word in str3.split()]
print(first_letters)
