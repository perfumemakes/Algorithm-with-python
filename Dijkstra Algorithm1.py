def solution(N, road, K):
    
    array = [[int(500000)] * N for _ in range(N)] 

    for i in range(N):
        array[i][i] = 0

    for road_ in road:
        if array[road_[0]-1][road_[1]-1] > road_[2]:
            array[road_[0]-1][road_[1]-1] = road_[2]
            array[road_[1]-1][road_[0]-1] = road_[2]

    visited = [False] * N
    visited[0] = True
    distance = array[0]

    for i in range(N):
        min_ = int(500000)
        index = 0
        for j in range(N):
            if not visited[j] and distance[j] < min_:
                min_ = distance[j]
                index = j
        if index == 0: 
            break

        visited[index] = True
        for k in range(N):
            if not visited[k]:
                if distance[index] + array[index][k] < distance[k]:
                    distance[k] = distance[index] + array[index][k]

    answer = 0

    for d in distance:
        if d <= K:
            answer += 1
    
    return answer

N=6
road=[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K=4
result=4

print(solution(N,road,K))
