def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x - 1)


print(f(3))
