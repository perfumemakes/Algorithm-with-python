n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key = lambda name:name[1], reverse=True)

for name in array:
    print(name[0], end=' ')