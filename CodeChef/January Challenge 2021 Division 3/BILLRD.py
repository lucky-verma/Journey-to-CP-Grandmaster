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
        N, K, x, y = map(int, input().split())
        b = min(x, y)
        x1 = x - b
        y1 = y - b
        # print(x1, y1)
        b2 = N - max(x, y)
        x2 = N
        y2 = y + b2
        # print(x2, y2)
        x3 = y2
        y3 = x2
        x4 = y1
        y4 = x1
        # print(x3, y3)
        # print(x4, y4)
        k = K % 4
        # print(K % 4)
        if x == N and y == 0:
            if k == 0 or 2:
                print(y, x)
            elif k == 1 or 3:
                print(x, y)
        elif x == 0 and y == N:
            if k == 0 or 2:
                print(y, x)
            elif k == 1 or 3:
                print(x, y)
        elif k == 0:
            print(x1, y1)
        elif k == 1:
            print(x2, y2)
        elif k == 2:
            print(x3, y3)
        elif k == 3:
            print(x4, y4)
