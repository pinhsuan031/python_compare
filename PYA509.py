# TODO
import math

x, y = eval(input())
m, n = eval(input())

p = x*n + m*y
q = y*n

def compute(p, q):
    return math.gcd(p, q)

a = compute(p, q)
p /= a
q /= a

print(f"{x}/{y} + {m}/{n} = {p:.0f}/{q:.0f}")