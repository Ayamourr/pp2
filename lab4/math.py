#ex1
import math

def deg_to_rad(d):
    return d * (math.pi / 180)

d = 15
r = deg_to_rad(d)
print(f"Output radian: {r}")

#ex2
def trapezoid_area(h, b1, b2):
    return ((b1 + b2) / 2) * h

h = 5
b1 = 5
b2 = 6

area = trapezoid_area(h, b1, b2)
print(f"Expected Output: {area}")

#ex3
def polygon_area(n, s):
    if n == 4:
        return s ** 2
    else:
        return (n * s ** 2) / (4 * math.tan(math.pi / n))

n = 4
s = 25

area = polygon_area(n, s)
print(f"The area of the polygon is: {area}")

#ex4 
def parallelogram_area(b, h):
    return b * h

b = 5
h = 6

area = parallelogram_area(b, h)
print(f"Expected Output: {area}")
