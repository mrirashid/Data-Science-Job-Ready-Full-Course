## fibonacci infinite sequenc 
## f(n) = f(n-1) + f(n-2)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for i in fibonacci():
    print(i)

