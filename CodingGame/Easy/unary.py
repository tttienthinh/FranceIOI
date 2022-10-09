import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

def int2bin(n):
    def aux(n):
        if n == 0:
            return ""
        if n%2 == 0:
            return aux(n//2) + "0"
        else:
            return aux(n//2) + "1"
    result = aux(n)
    result = (7-len(result)) * "0" + result
    return result

def ascii2bin(s):
    return int2bin(ord(s))

def text2bin(t):
    b = ""
    for s in t:
        b += ascii2bin(s)
    return b

def number(s):
    if s == "1":
        return "0"
    else:
        return "00"

b = text2bin(message)
result = ""
c = 0
prev = None
for s in b:
    if prev is None:
        result += number(s)
        prev = s
        c += 1
    elif s == prev:
        c += 1
    else:
        result += " " + c*"0" + " " + number(s)
        prev = s
        c = 1

result += " " + c*"0"


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)
