import math

def calculate(mass):
    return math.floor(mass / 3) - 2

modules = list(map(int, open('day1/input.txt','r').read().split('\n')))
result = []

for x in modules:
    mass = x
    
    while mass > 0:
        mass = calculate(mass)
        result.append(mass) if mass > 0 else None

print(sum(result))