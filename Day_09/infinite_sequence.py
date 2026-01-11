## the infinite sequence

def infinite_loop():
    i=0 
    while True:
        yield i 
        i = i + 1 
