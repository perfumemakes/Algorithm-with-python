from itertools import combinations

def solution(relation):
    row_size, col_size = len(relation), len(relation[0])
    ans = []
    
    # 가능한 모든 열들의 인덱스 조합을 각 행에 대입
    for c in range(1, col_size + 1):
        for col in combinations(range(col_size), c):
            check = []
            for row in relation:
                temp = []
                for idx in col:
                    temp.append((row[idx]))
                check.append(tuple(temp))

            # 유일성 체크
            if len(set(check)) == row_size:
                if any([set(col).issuperset(set(a)) for a in ans]):
                    continue
                # 최소성 체크
                else:
                    ans.append(col)       

    return len(ans)