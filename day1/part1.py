import math

modules = list(map(int, open('day1/input.txt','r').read().split('\n')))

print (sum([math.floor(x / 3) - 2 for x in modules]))