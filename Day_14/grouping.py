from itertools import groupby
items=[{'c':'x'},{'c':'x'},{'c':'y'}]
items=sorted(items,key=lambda x:x['c'])

for k,g in groupby(items,key=lambda x:x['c']): print(k,list(g))