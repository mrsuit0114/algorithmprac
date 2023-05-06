import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')

# 이걸 dictionary를 쓰네

# import sys

# input = sys.stdin.readline

# n = int(input())
# graph =[[] for i in range(n)]
# visit = [0]*n

# def preord(idx):
#     if visit[idx]==0:
#         print(chr(ord("A")+idx),end="")
#         visit[idx]=1
#         if graph[idx]:
#             preord(graph[idx][0])  # 없으면 가지말아야하는데 근데 방문했다면 알아서 처리할건데
#             preord(graph[idx][-1])

# def inord(idx):
#     if visit[idx]==0:
#         inord(graph[idx][0])
#         print(chr(ord("A")+idx),end="")
#         inord(graph[idx][-1])

# def postord(idx):
#     if visit[idx]==0:
#         postord(graph[idx][0])
#         postord(graph[idx][-1])
#         print(chr(ord("A")+idx),end="")

# for i in range(n):
#     a,b,c = map(str,input().split())
#     if b!=".":
#         graph[ord(a)-ord("A")].append(ord(b)-ord("A"))
#         # graph[ord(b)-ord("A")].append(ord(a)-ord("A"))
#     if c!=".":
#         graph[ord(a)-ord("A")].append(ord(c)-ord("A"))
#         # graph[ord(c)-ord("A")].append(ord(a)-ord("A"))

# preord(0)
# inord(0)
# postord(0)

# print(graph)


