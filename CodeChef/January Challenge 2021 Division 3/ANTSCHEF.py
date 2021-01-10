"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------- fast io --------------------
if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        lst = []
        for _ in range(N):
            lst.append(list(map(int, input().split())))
        # print(N, lst)
        p = 0
        n = 0
        s = 0
        if N == 1:
            for k in lst[0]:
                if k >= 0:
                    p += 1
                else:
                    n += 1
            if lst[0] == 0:
                print(0)
            while n and p > 0:
                s = s + n + p - 1
                n -= 1
                p -= 1
            print(s)


"""
C++ partial solution
"""

# #include <bits/stdc++.h>
# using namespace std;
#
# int main() {
# 	// your code goes here
# 	ios_base::sync_with_stdio(false);
# 	cin.tie(NULL);
# 	int k;
# 	cin>>k;
# 	while(k--){
# 	    int N;
# 	    cin>>N;
# 	    int M;
# 	    cin>>M;
# 	    long long int arr[M];
# 	    for(int i=0; i<M; i++){
# 	        cin>>arr[i];
# 	    }
# 	    long long int p=0, n=0, sum=0;
# 	    if (N==1){
# 	        sort(arr, arr+M);
# 	        if(arr[0]>0)cout<<0<<endl;
# 	        else if(arr[M-1]<0)cout<<0<<endl;
# 	        else{
# 	            for(int i=0;i<M; i++){
# 	                if(arr[i]>0){
# 	                    n=i;p=M-i;break;
# 	                }
# 	            }
# 	            while(n>0 && p>0){
# 	                sum = sum + n + p - 1;
# 	                n--;
# 	                p--;
# 	            }
# 	            cout<<sum<<endl;
# 	        }
# 	    }
# 	}
# 	return 0;
# }
