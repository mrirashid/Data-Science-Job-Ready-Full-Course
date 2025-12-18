Data=[10,20,30,40,50];

## slicing the items
reverse=Data[-1:-4:-1]; ## shows last 3 items , start from the end
print(f"Reverse items: {reverse}");
slicing= Data[2::] ## shows index 2 to end
print(f"Slicing items: {slicing}");

slicing2= Data[:1:-1]; ## shows last 3 items , start from the end
print(f"Slicing items: {slicing2}");
