def fac(n):
  if n == 0:
    return 1
  return fac(n-1)*n

x = float(input())

print(fac(int(x))*(int(x)+1)**(x-int(x)))
