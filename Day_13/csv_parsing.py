import csv
w=csv.writer(open('c.csv','w',newline=''))
w.writerow(['n','a'])
w.writerow(['A',1])

for r in csv.DictReader(open('c.csv')): 
    print(r)
