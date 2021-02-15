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
    # Write your solution here
    for _ in range(int(input())):  # takes the input cases

        def timeConversion(s):
            if "PM" in s:
                s = s.replace("PM", "")
                t = s.split(":")
                if t[0] != '12':
                    t[0] = str(int(t[0]) + 12)
                    s = "".join(t)
                return s
            else:
                s = s.replace("AM", "")
                t = s.split(":")
                if t[0] == '12':
                    t[0] = '00'
                    s = "".join(t)
                return s

        meeting = str(input())
        n = int(input())
        ans = []
        for i in range(n):
            slab = str(input())
            start = timeConversion(slab[:len(slab) // 2])
            end = timeConversion(slab[len(slab) // 2:])
            meet = timeConversion(meeting)
            if ":" in meet:
                start = meet.replace(":", "")
            if ":" in start:
                start = start.replace(":", "")
            if ":" in end:
                end = end.replace(":", "")

            if int(start) <= int(meet) <= int(end):
                ans.append(1)
            else:
                ans.append(0)
        ANS = int(''.join(map(str, ans)))
        print(ANS)

