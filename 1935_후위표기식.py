N = int(input())
s = input()
sl = []
for i in s:
    sl.append(i)
li = [int(input()) for _ in range(N)]
dic = {}
j = 0
for i in range(len(s)):
    if sl[i].isalpha():
        if sl[i] not in dic:
            dic[sl[i]] = li[j]
            j +=1
        sl[i] = dic[s[i]]

stack = []
for i in range(len(sl)):
    if str(sl[i]) != sl[i] : # 정수면
        stack.append(sl[i])
    else:
        b = stack.pop()
        a = stack.pop()
        if sl[i] == '+':
            stack.append(a+b)
        elif sl[i] == '-':
            stack.append(a-b)
        elif sl[i] == '*':
            stack.append(a*b)
        elif sl[i] == '/':
            stack.append(a/b)

print("%.2f" %stack[0])