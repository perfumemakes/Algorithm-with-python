def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    print("mid:", mid)
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
n, target = list(map(int, input().split()))
print("target:", target)
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("It's None!")
else:
    print(result +1)


    
