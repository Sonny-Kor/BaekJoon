name = list(input().split("-"))
result = []
for i in name:
    result.append(i[0])
print("".join(result))