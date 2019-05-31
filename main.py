def fac(x):
    def factorial(n):
        n = int(n)
        if n == 0:
            return 1
        return factorial(n - 1) * n

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
            return factorial(int(x)) * (int(x) + 1) ** (x - int(x))
        except OverflowError:
            return "Error: factorial goes beyond float type"
