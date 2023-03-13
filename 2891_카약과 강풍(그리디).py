# N, S, R = map(int,input().split(" "))
# arr = [1 for _ in range(N)] #현재 상태

# S_Arr = list(map(int,input().split(" "))) #고장남

# for s in S_Arr:
#     if (s-1) >= 0:
#         arr[s-1] = 0

# R_Arr = list(map(int,input().split(" "))) #여유분
# for i in range(R):
#     R_Arr[i] -= 1

# for i in R_Arr: #자기꺼 고장 체크 , 옆팀 챙겨주기 
#     if arr[i] == 0: # 자기
#         arr[i] = 1
#         R_Arr.remove(i)
#         continue
#     if i-1 != 0:
#         if arr[i-1] == 0:
#             arr[i-1] = 1
#             R_Arr.remove(i)
#             continue
#     if i+1 != 0:
#         if arr[i+1] == 0:
#             arr[i+1] =1 
#             R_Arr.remove(i)
#             continue
# result = 0
# for i in arr:
#     if i == 0:
#         result += 1
# print(result)
# N,S,R = map(int, input().split())
# S = list(map(int, input().split())) # 카약이 손상된 팀 번호
# R = list(map(int, input().split())) # 카약이 남는 팀 번호

# result = 0 # 출발하지 못하는 팀 수

# for i in S:
#     if i-1 in R:
#         R.remove(i-1)
#     elif i+1 in R:
#         R.remove(i+1)
#     else:
#         result+=1
        
# print(result)

