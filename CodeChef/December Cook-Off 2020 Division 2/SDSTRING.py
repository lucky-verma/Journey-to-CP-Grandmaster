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

    # for _ in range(int(input())):
    #     binaryStr = list(input())
    #     for i in range(0, len(binaryStr) - 1):
    #         try:
    #             if binaryStr[i] == '0' and binaryStr[i + 1] == '1':
    #                 print('THERE at ' + str(i) + ',' + str(i + 1))
    #                 binaryStr.pop(i)
    #                 print(binaryStr)
    #                 binaryStr.pop(i)
    #                 print(binaryStr)
    #         except:
    #             pass

    for _ in range(int(input())):
        s = str(input())
        if len(s) & 1 == 1:
            print(-1)
        else:
            zeroes = 0
            ones = 0
            for i in range(len(s)):
                if s[i] == '0':
                    zeroes += 1
                else:
                    ones += 1
            if zeroes == ones:
                print(0)
            elif (zeroes or ones) != len(s):
                print(int(abs(zeroes - ones) / 2))
            else:
                print(-1)

    pass
