def flat(l):
 r=[]
 for x in l:
  if isinstance(x,list): r+=flat(x)
  else: r.append(x)
 return r
print(flat([1,[2,[3,4]]]))