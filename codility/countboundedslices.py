import heapq

def solution(K,A):
    
            



# def solution(K,A):
#     ans = 0
#     ex=[]
#     for i in range(len(A)):
#         minheap = []
#         maxheap = []
#         count = i
#         while count<len(A):
#             heapq.heappush(minheap,A[count])
#             heapq.heappush(maxheap,-A[count])
#             m = -maxheap[0]
#             n = minheap[0]
#             if m-n<=K:
#                 ex.append([i,count])
#                 count+=1
#             else:
#                 break
#     ans = len(ex)
#     return(ans)

solution(2,[3,5,7,6,3])
    


#해당 구간에서 최대와 최소를 항상 갱신해서 알수있도록 최소힙 최대힙 두개 운영
#(a,b)는 가능하고 (a,b+1)에서 불가능하다면 총 몇개의 경우가 나오나? a<=b
#a,a ... a,b 까지 b-a+1개 ... 1개까지 --> (b-a+1)(b-a+2)/2
#idx시작점이 바뀌면 힙을 다시 초기화 해주는게 편할듯