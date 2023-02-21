#https://www.acmicpc.net/problem/1715
#카드정렬하기

class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None) # 첫 idx는 1을 기준으로 
    
    def check_swap(self, idx):
        if idx <= 1:
            return False
        
        parent_idx = idx//2 # 부모 인덱스
        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        self.heap.append(data)
        idx = len(self.heap) -1

        while self.check_swap(idx):
            parent_idx = idx//2
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        return True

    def check_swap_down(self,idx):
        left_idx = idx*2
        right_idx = idx * 2 +1
        
        # 자식 노드가 없는 경우
        if left_idx >= len(self.heap):
            return False
        
        # self.flag 는 1인경우 왼쪽과 부모 변경, 2인경우 오른쪽과 부모 변경
        # 왼쪽에만 있는 경우
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
        # 왼쪽 오른쪽 모두 자식이 있는 경우
        else:
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    self.flag = 1 
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx] > self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False
    
    def pop(self):
        if len(self.heap) <= 1:
            return None
        
        max = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        self.flag = 0
        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1
            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        return max

MyHeap = Heap()
MyHeap.insert(5)
MyHeap.insert(7)
MyHeap.insert(1)
MyHeap.insert(4)
MyHeap.insert(2)
MyHeap.insert(8)

print(MyHeap.pop())
