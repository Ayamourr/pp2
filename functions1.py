#ex1
def gram_to_ounce():
    gram = int(input())
    ounce = 28.3495231 * gram
    return ounce

result = gram_to_ounce()
print(result)

#ex2
def faren():
    cell = int(input())
    cent = C = (5 / 9) * (cell - 32)
    return cent

result = faren()
print(result)

#ex3
def kol(n_heads, n_legs):
    for n_chicken in range(n_heads+1):
        n_rabbit = n_heads - n_chicken
        if 2*n_chicken + 4*n_rabbit == n_legs:
            return n_chicken, n_rabbit

n_heads = 35
n_legs = 94
print(kol(n_heads, n_legs))

#ex4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    num_list = map(int, numbers.split())
    prime_numbers = filter(is_prime, num_list)

    return list(prime_numbers)

numbers = "3 4 5 6 7 11 13"
prime_numbers = filter_prime(numbers)
print(prime_numbers)

#ex5
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)


users_input=str(input())
get_permutation(users_input)

#ex6
def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))

input_sentence = "We are ready"
reversed_sentence = reverse_sentence(input_sentence)
print(reversed_sentence)

#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True  
    return False 

#ex8
def spy_game(nums):
    pattern = [0, 0, 7]
    
    for num in nums:
        if num == pattern[0]:  
            pattern.pop(0)  
        if not pattern: 
            return True
    return False

#ex9
import math

def sphere_volume(radius):

    return (4.0/3.0) * math.pi * (radius ** 3)

#ex10
def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

#ex11
def palindrome(string):
    s=string[::-1]
    if s==string:
        print(True)
    else:
        print(False)
    
phrase=input()
palindrome(phrase)

#ex12
def histogram(lst):
    for number in lst:
        print('*' * number)

histogram([4, 9, 7])

#ex13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break 

guess_the_number()

#ex14
from my_functions import palindrome, unique_elements, histogram

print(palindrome("Madam")) 

print(unique_elements([1, 2, 2, 3, 4, 4, 5])) 

histogram([3, 5, 2])  

