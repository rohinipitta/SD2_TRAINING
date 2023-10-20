a=list(map(int,input().split()))
n=len(a)
f=[]
l=[]
k=int(input())
l=a[k:n]
f.extend(a[0:k])
print(*l+f)
