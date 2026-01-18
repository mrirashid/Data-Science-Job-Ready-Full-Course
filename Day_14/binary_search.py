def bs(a,t):
 l,r=0,len(a)-1
 
 while l<=r:
  m=(l+r)//2
  if a[m]==t: return m
  if a[m]<t: l=m+1
  else: r=m-1
 return -1
print(bs([1,2,3,4],3))