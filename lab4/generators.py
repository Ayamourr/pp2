#ex1
def sqr_gnrt(n):
    i = 1
    while i ** 2 <=n:
        yield i ** 2
        i+=1

n = int(input())
generator = sqr_gnrt(n)
for square in generator:
    print(square)

#ex2 
def even_numbers(n):
    for i in range (0, n+1):
        if i % 2 == 0:
            yield i
        
n = int(input())
generator = even_numbers(n)
print (",".join(map(list, generator)))

#ex3
def div_by_3_and_4(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in div_by_3_and_4(100):
    print(num)

#ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

for value in squares(1, 5):
    print(value)

#ex5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(10):
    print(num)
