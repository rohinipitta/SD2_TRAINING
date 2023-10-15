n=int(input("enter thr capacity:"))
print("Enter weights:")
weights=list(map(int,input().split()))
print("Enter profits:")
profits=list(map(int,input().split()))
l=list(zip(weights,profits))
l.sort(key=lambda x:x[1]/x[0],reverse=True) #according to 2nd index element pw,
#the list is sorted in reverse order, descending order
print(list(l)) #(w,p,pw)
maxpr=0
for wt,pr in l:
    if wt<=n:
        maxpr+=pr
        n-=wt
    else:
        maxpr+=n*(pr/wt)
        break
print(maxpr)
