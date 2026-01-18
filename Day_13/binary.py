with open('bin.dat','wb') as f:
    f.write(b'I am rashid')

with open('bin.dat','rb') as f:
    print(f.read())