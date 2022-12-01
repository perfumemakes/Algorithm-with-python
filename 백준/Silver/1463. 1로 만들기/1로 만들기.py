import sys

input = sys.stdin.readline
N=int(input())
    
dp={1:0}
def rec(N):
    if N in dp.keys():
        return dp[N]
    if (N%3==0) and (N%2==0):
        dp[N]=min(rec(N//3)+1, rec(N//2)+1)
    elif N%3==0:
        dp[N]=min(rec(N//3)+1, rec(N-1)+1)
    elif N%2==0:
        dp[N]=min(rec(N//2)+1, rec(N-1)+1)
    else:
        dp[N]=rec(N-1)+1
    return dp[N]


if __name__=="__main__":
    print(rec(N))