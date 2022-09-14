record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
dict={}
chat = []
enter_msg = "%s님이 들어왔습니다."
leave_msg = "%s님이 나갔습니다."

for i in record:
    word = i.split(" ")
    if word[0] == "Enter":
        dict[word[1]]=word[2]
        chat.append([enter_msg, word[1]])
    elif word[0] == "Leave":
        chat.append([leave_msg, word[1]])
    else:
        dict[word[1]]=word[2]
        
for i in chat:
    print(i[0] % dict[i[1]])
   

