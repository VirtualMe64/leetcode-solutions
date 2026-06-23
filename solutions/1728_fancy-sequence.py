# Problem: https://leetcode.com/problems/fancy-sequence
# Runtime: 165 ms

class Fancy:
    N = 10 ** 9 + 7
    def __init__(self):
        # total effect of applying all mults and adds
        self.cumulativeOps = [1, 0] # 1x + 0
        self.sequence = []

    def append(self, val: int) -> None:
        # must find value x, s.t ax + b % N = val % N
        # ax + b % N = val % N
        # ax % N = (val - b) % N
        # find modular inverse of a w.r.t N: a'
        # x = a'(val - b) % N
        a_prime = pow(self.cumulativeOps[0], -1, self.N)
        x = (a_prime * (val - self.cumulativeOps[1])) % self.N
        self.sequence.append(x)

    def addAll(self, inc: int) -> None:
        # given: (ax + c) % N
        # change: (ax + c) % N + inc % N
        # new: (ax + (c + inc) % N)
        newAdd = (self.cumulativeOps[1] + inc) % self.N
        self.cumulativeOps[1] = newAdd

    def multAll(self, m: int) -> None:
        # given: (ax + c) % N
        # change: ((ax + c) * m) % N
        # new: ((a * m) % N)x + (c * m) % n
        newMult = (self.cumulativeOps[0] * m) % self.N
        newAdd = (self.cumulativeOps[1] * m) % self.N
        self.cumulativeOps = [newMult, newAdd]

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        base = self.sequence[idx]
        return ((base * self.cumulativeOps[0]) + self.cumulativeOps[1]) % self.N


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)