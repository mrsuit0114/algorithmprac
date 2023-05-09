from math import gcd
import sys

a, b = map(int,sys.stdin.readline().split())

g = gcd(a,b)
b = a//g * b//g * g

print(g)
print(b)