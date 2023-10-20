a=list(map(int,input().split()))
n=len(a)
k=int(input())
for i in range(k):
    a.insert(0,a.pop())
print(a)
