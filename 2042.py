import math 
import sys

# 입력 리스트를 세그먼트 트리로 구성하기 전 초기화 하는 함수
def Seg_tree_const(list, n): 
    height = int(math.ceil((math.log2(n)))) # 세그먼트 트리의 높이 설정
    t_size = int(2* math.pow(2, height) - 1)  # 세그먼트 트리의 배열의 크기 설정
    seg_tree = [0 for i in range(t_size)] # 세그먼트 트리를 구성하는 배열 초기화
    Construct_tree(list, 0, n-1, seg_tree, 0) # 세그먼트 트리 구현함수 호출
    return seg_tree

#  입력 리스트를 세그먼트 트리로 만들고 반환하는 함수
def Construct_tree(list,start,end,seg_tree,current):
    if start == end : # 모두 분할 시킨 경우
        seg_tree[current] = list[start]  # 분할 시켜진 기존의 원소들을 Segment_tree에 입력
        return list[start]
    mid = start + (end-start) // 2
    child = 2 * current
    seg_tree[current] = Construct_tree(list, start, mid, seg_tree, child+1)  + Construct_tree(list,mid+1,end,seg_tree,child+2)
# 재귀함수를 통해 왼쪽자식과 오른쪽 자식의 합을 부모노드에 입력
    return seg_tree[current]

# 세그먼트 트리를 사용하여 부분 합을 계산하기 전 함수
def Get_query(seg_tree, n, q_s, q_e):
    if q_s <0 or q_e > n-1 or q_e < q_s : # 인자 값이 문제없는지 확인하는 부분
        return
    sum = Query_Sum(seg_tree,0,n-1,q_s,q_e,0)
    return sum

# 세그먼트 트리를 사용하여 부분 합을 계산
def Query_Sum(seg_tree, start, end , q_s , q_e , current):
    if q_s <= start and q_e >= end: # 구간이 범위 안
        return seg_tree[current]
    if end < q_s or start > q_e: # 부분 합을 계산하는 범위 밖인 경우
        return 0
    mid = start + (end - start) // 2 
    child = current * 2
    return Query_Sum(seg_tree,start,mid,q_s,q_e,child+1) + Query_Sum(seg_tree,mid+1,end,q_s,q_e,child+2)
    # 자식 노드 왼쪽과 오른쪽으로 분할 시키고 마지막에 구간인 부분만 더하기

# 입력 리스트의 값이 변경되었을 때 세그먼트 트리를 갱신
def Segtree_update(seg_tree, start, end , i , d_value , current):
    if  i < start or i > end:     # 업데이트 하려는 idx가 범위 밖인 경우
        return
    seg_tree[current] = seg_tree[current] + d_value # index가 영향을 주는 범위 안일 경우 더하기

    if start != end: 
        mid = start + (end -start)//2
        child = 2* current
        Segtree_update(seg_tree,start,mid,i,d_value,child+1) 
        Segtree_update(seg_tree,mid+1,end,i,d_value,child+2) 
# 자식노드 왼쪽과 오른쪽노드 를 나눠서 재귀함수를 호출하고 조건을 만족한다면 	d_value만큼 업데이트


N ,M, K = map(int,sys.stdin.readline().split(' '))
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

seg_tree = Seg_tree_const(arr,len(arr))
# print(seg_tree)
for _ in range(M+K):
    a,b,c = map(int,sys.stdin.readline().split(' '))
    if a == 1: # b를 c로 변경
        dvalue = c-arr[b-1]
        arr[b-1]=c
        Segtree_update(seg_tree,0,N-1,b-1,dvalue,0)
        # print(seg_tree)
    elif a == 2: # b부터 c까지 합 구하기
        print(Get_query(seg_tree,N,b-1,c-1))
        # print(seg_tree)
