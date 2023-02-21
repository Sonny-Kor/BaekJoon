# while 1:
#     try:
#         cycle_num = input().rstrip()
#         checking = 0
#         for i in range(len(cycle_num)):
#             next_num = str(int(cycle_num)*(i+1)).zfill(len(cycle_num))
#             if sorted(cycle_num) == sorted(next_num):
#                 checking += 1
#         if checking == len(cycle_num):
#             print(cycle_num+" is cyclic")
#         else:
#             print(cycle_num+ " is not cyclic") 
#     except:
#         break

import sys
from collections import deque

index = sys.stdin.readline().strip()

for i in range(1,len(index)+1):
    comp_index=(str((int(index))*i)).zfill(len(index))
    if comp_index not in index*2:
        print(index,"is not cyclic")
        exit()
print(index,"is cyclic")