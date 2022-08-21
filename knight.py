print(ord('a'))

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-96
count = 0

steps=[(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if (1<=next_row<=8 and 1<=next_column<=8):
        count+=1
        
print(count)