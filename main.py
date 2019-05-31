# Private method for finding factorial
def factorial(n):
    n = int(n)
    if n == 0:
        return 1
    return factorial(n - 1) * n

# Private method for check is prime number or return 1
def isprnum(x):
    if x > 1:
        out = True
        for i in range(2, x):
            if x % i == 0:
                out = False
        if out:
            return x

    return 1

# Factorial
def fac(x):
    if x < 0:
        return "Error: number < 0"
    elif (x >= 0) and (x <= 1):
        return 1
    elif int(x) == x:
        try:
            return factorial(x)
        except RecursionError:
            return "Error: large number"
    else:
        try:
            # Search factorials fractional numbers
            return factorial(int(x)) * (int(x) + 1) ** (x - int(x))
        except OverflowError:
            return "Error: factorial goes beyond float type"

# Multi factorial
def multf(x, m):
    out = x
    i = 0

    while i < int(m):
        out = fac(out)
        i += 1
    return out

# Super factorial
def supf(m):
    out = 1
    for x in range(2, int(m)+1):
        out *= fac(x)
    return out

# Primorial
def prim(m):
    out = 1
    i = 1
    for k in range(int(m)):
        while True:
            if isprnum(i) != 1:
                out *= i
                i += 1
                print(i)
                break
            else:
                i += 1
    return out
