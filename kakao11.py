"""
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k= 2
ban_list=[]

report=list(dict.fromkeys(report))

for i in range(len(report)):
    report[i] = report[i].split(" ")

for i in range(len(id_list)):
    cnt = 0
    for j in report:
        if id_list[i]==j[1]:
            cnt += 1
            if cnt>= k:
                ban_list.append(id_list[i])
                break
answer = []

for i in id_list:
    cnt=0
    for j in report:
        if j[0]==i and j[1] in ban_list:
            cnt+=1
    answer.append(cnt)
"""
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k= 2
    
stop = []
answer = [0] * len(id_list)
dicReports = {id: [] for id in id_list}

for i in set(report):
    report2 = i.split(' ')
    stop.append(report2[1])
    dicReports[report2[0]].append(report2[1])

stop = set([i for i in stop if stop.count(i) >= k])
print(dicReports)
for key, value in dicReports.items():
    for s in stop:
        if s in value:
            answer[id_list.index(key)] += 1


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for r in set(report):
        a, b = r.split()
        reported[b] += 1

    for r in set(report):
        a, b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer
