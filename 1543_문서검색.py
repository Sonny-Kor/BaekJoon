Doc = input()
Word = input()
sw1 = True
new_Doc = []
    
start=0
result=0
while(True):
    start=Doc.find(Word,start)
    if(start == -1):
        break
    start += len(Word)
    result+=1
print(result)