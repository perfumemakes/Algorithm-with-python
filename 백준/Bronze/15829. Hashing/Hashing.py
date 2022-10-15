Length=int(input())
arr=str(input())

answer=0
for i in range(Length):
    answer+=(ord(arr[i])-96)*31**i

print(answer%1234567891)