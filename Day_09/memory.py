## compare sys.getsize () list comprehension vs generator expression
import sys
number=1000000;

list_comparison=[x for x in range(number)]
print(f"List comparison: {list}")
print(sys.getsizeof(list_comparison))       
generator=(x for x in range(number))
print(f"Generator comparison: {generator}")    
print(sys.getsizeof(generator))    

