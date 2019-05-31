def fac(x):
    def factorial(n):
        if n == 0:
            return 1
        return factorial(n - 1) * n

    return factorial(int(x)) * (int(x) + 1) ** (x - int(x))
