for _ in range(int(input())):
    L,R = map(int,input().split())
    ans = 2 *(abs(L-R))
    print(ans+1)