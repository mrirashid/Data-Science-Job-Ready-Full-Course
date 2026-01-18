with open('u.txt','w',encoding='utf-8') as f:
    f.write('Hi 🌍')

with open('u.txt','r',encoding='utf-8') as f:
    print(f.read())