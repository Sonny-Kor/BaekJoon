result = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

word = input()
for index, alpha in enumerate(word):
    idx = ord(alpha) - 97
    if result[idx] == -1:
        result[idx] += index+1

for a in result:
    print(a, end=" ")
