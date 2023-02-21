import sys

a, b = map(int,sys.stdin.readline().split(' '))
count = 0
while(a < b):
    if b%2 == 0:
        b = b / 2
        count += 1
    else:
        b = (b-1)/10
        count += 1
if b != a:
    print(-1)
else:
    print(count+1)