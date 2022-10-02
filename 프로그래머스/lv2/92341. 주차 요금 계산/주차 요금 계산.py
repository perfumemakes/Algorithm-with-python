import math

def solution(fees, records):

    records=[records[i].split(" ") for i in range(len(records))]
    for i in range(len(records)):
        records[i][0] = int(records[i][0].split(":")[0]) * 60 + int(records[i][0].split(":")[1])   
    for i in range(len(records)):
        if records[i][2] == "IN":
            records[i][0] = (-1)*records[i][0]

    cars=[]
    for i in range(len(records)):
        if records[i][1] not in cars:
            cars.append(records[i][1])
    cars= sorted(cars, key = lambda x:x)

    for i in cars:
        count=0
        for j in range(len(records)):
            if records[j][1] == i:
                if records[j][2]=="IN":
                    count-=1
                if records[j][2]=="OUT":
                    count+=1
        if count<0:
            records.append([23*60+59, i, "OUT"])

            
    answer=[]
    for i in cars:
        number=0
        for j in range(len(records)):
            if i == records[j][1]:
                number+=int(records[j][0])
        answer.append(number)

    for i in range(len(answer)):
        if answer[i] <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = math.ceil((answer[i]-fees[0])/fees[2])*fees[3] + fees[1]
    
    return answer