def solution(new_id):
    new_id = new_id.lower()
    rule=["-","_","."]
    id=""

    for i in new_id:
        if i.isalpha() or i in rule:
            id=id+i

    while id.count("..")>0:
        id=id.replace("..",".")

    if id[0] == ".":
        if len(id) ==1:
            return "aaa"
        else:
            id=id[1:]
            
    if id[-1] == ".":
        if len(id) ==1:
            return "aaa"
        else:
            id = id[:-1]
    if id =="":
        id = "a"
    if len(id)>= 16:
        id = id[0:15]
    if id[-1] == ".":
        id = id[0:-1]
    while len(id)<3:
        id=id+id[-1]
    return id

solution("=.=")
