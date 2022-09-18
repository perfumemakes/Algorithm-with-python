s = "one4seveneight"
dict={}
word=['zero','one','two','three','four','five','six','seven','eight','nine']
for i in range(len(word)):
    dict[word[i]] = i

result=''
change=''

for i in s:
    if i.isdigit():
        result+=i
    elif i.isalpha():
        change+=i
        if change in dict.keys():
            result+=str(dict[change])
            change=''

print(int(result))