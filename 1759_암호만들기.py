L, C = map(int,input().split(" "))
password = list(input().split(" "))
password.sort()
need_token = ['a','e','i','o','u']
answer = []

def check(word):
    if len(word) == L:
        count1 = 0
        count2 = 0
        for i in word:
            if i in need_token: # 모음
                count1 = count1 + 1  
            else: # 자음
                count2 = count2 + 1
        if count1 >= 1 and count2 >=2:
            print("".join(answer))


def dfs(idx):
    for i in range(idx,C):
        answer.append(password[i])
        check(answer)
        dfs(i+1)
        answer.pop()
dfs(0)
