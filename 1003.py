
fibolist = [0, 1]
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        global fibolist
        if len(fibolist) > n:
            return fibolist[n]
        else:
            fibo = fibonacci(n-1) + fibonacci(n-2)
            fibolist.append(fibo)
            return fibo

T = int(input())
test = []
for i in range(T):
    test.append(int(input()))
for i in test:
    if i > 0:
        k = fibonacci(i)
        print("%d %d" %(fibolist[i-1],k))
    elif i == 0:
        print("1 0")