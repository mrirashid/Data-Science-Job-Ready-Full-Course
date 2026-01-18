with open('log.txt','w')as f:
    f.write('One\n')

with open('log.txt','a') as f:
    f.write('Two\n')
try:
    open('log.txt','x')
except FileExistsError:
    print('Exists')

    