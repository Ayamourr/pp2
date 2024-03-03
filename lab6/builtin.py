#1
from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x*y, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply(numbers)
print(result)

#2
def count(s):

    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

string = "Hello, World!" 
upper_count, lower_count = count(string)
print(upper_count)
print(lower_count)

#3
def is_palindrome(s):

    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

input_string = "A man, a plan, a canal, Panama"
if is_palindrome(input_string):
    print("palindrome.")
else:
    print("not palindrome.")

#4
import time
import math

def delayed_sqrt(number, delay_ms):

    delay_s = delay_ms / 1000.0
    time.sleep(delay_s)
    sqrt_value = math.sqrt(number)
    return sqrt_value

number = 25100
delay_ms = 2123

sqrt_value = delayed_sqrt(number, delay_ms)
print(sqrt_value)

#5
def true(elements):

    return all(elements)

tuple = [
    (True, True, True), 
    (True, False, True), 
    (1, 2, 3), 
    (0, 1, 2), 
]

for t in tuple:
    result = true(t)
    print(result)



