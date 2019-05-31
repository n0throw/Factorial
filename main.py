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
        if x >= 997:
            return "Error: number >= 997"
        return factorial(x)
    else:
        if x >= 170.62421348621231:
            return "Error: factorial goes beyond float type"
        return factorial(int(x)) * (int(x) + 1) ** (x - int(x))
