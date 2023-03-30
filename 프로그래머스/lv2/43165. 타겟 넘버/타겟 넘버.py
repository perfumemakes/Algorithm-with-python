def recur(numbers, target, idx, empty_list, cnt):
        if idx == len(numbers):
            if sum(empty_list) == target:
                cnt.append(1)
            return
        empty_list.append(-int(numbers[idx]))
        #print(empty_list)
        idx += 1
        recur(numbers, target, idx, empty_list, cnt)
        idx -= 1
        empty_list.pop()
        empty_list.append(int(numbers[idx]))
        #print(empty_list)
        idx += 1
        recur(numbers, target, idx, empty_list, cnt)
        idx -= 1
        empty_list.pop()
        
def solution(numbers, target) -> int:
    empty_list = []
    cnt = []
    recur(numbers, target, 0, empty_list, cnt)
    return sum(cnt)

def solution2(numbers, target):
    
    start=[0]
    for i in numbers:
        end=[]
        for j in start:
            end.append(j+i)
            end.append(j-i)
            start=end
    return start.count(target)