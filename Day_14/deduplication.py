def dedup(l):
 s=set();r=[]
 for x in l:
  if x not in s: s.add(x); r.append(x)
 return r
print(dedup([1,1,1]))