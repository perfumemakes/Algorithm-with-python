import heapq

def solution(m, musicinfos):

    answer: list = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for i in range(len(musicinfos)):
        temp = list(map(str, musicinfos[i].split(",")))
        temp[3] = temp[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        time = (int(temp[1][:2]) - int(temp[0][:2])) * 60 + (int(temp[1][3:]) - int(temp[0][3:]))

        if time <= len(temp[3]):
            music = temp[3][:time+1]
            if m in music:
                heapq.heappush(answer, (-len(music), temp[2]))
        else:
            i: int = time // len(temp[3])
            v: int = time % len(temp[3])
            music = temp[3]*i + temp[3][:v]
            if m in music:
                heapq.heappush(answer, (-len(music), temp[2]))

    if answer:
        print(answer)
        return heapq.heappop(answer)[1]
    else:
        return "(None)"