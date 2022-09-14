array1 = [5,7,9,0,3,1,6,2,4,8]
array2=[7,5,9,0,3,1,6,2,9,1,8,0,5,2]

def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    print("pivot:" ,pivot)
    tail = array[1:]
    print("tail:", tail)
    
    left_side = [x for x in tail if x<= pivot]
    print("left:", left_side)
    right_side = [x for x in tail if x> pivot]
    print("right:", right_side)
    
    return quicksort(left_side) + [pivot] + quicksort(right_side)


def countsort(array):
    count = [0]*(max(array)+1)
    print("count:", count)
    
    for i in range(len(array)):
        count[array[i]] +=1 
    print("count", count)
        
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
            
def setting(data):
    return data[1]

array3 =[('banana', 2),('apple',5),('carrot', 3)]


result=sorted(array3, key=setting)
print(result)
