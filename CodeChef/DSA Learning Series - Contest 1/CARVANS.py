"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
if __name__ == "__main__":
    for _ in range(int(input())):
        """
        Option 1:
        """
        n = int(input())
        s = list(map(int, input().split()))
        if n == 1:
            print(n)
        else:
            c = 1
            for i in range(1, n):
                if s[i] <= s[i - 1]:
                    c += 1
                else:
                    s[i] = s[i - 1]
            print(c)
    pass

"""
option 2:
"""
# # cook your dish here
# for _ in range(int(input())):
#     N = int(input())
#     if N == 1:
#         print(1)
#     else:
#         speeds = list(map(int, input().split()))
#         m = 1
#         for j in range(1, N):
#             if m <= int(speeds[j]) - int(speeds[j - 1]):
#                 m += 1
#             else:
#                 speeds[j] = speeds[j - 1]
#         print(m)
