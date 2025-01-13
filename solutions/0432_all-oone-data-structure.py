# Problem: https://leetcode.com/problems/all-oone-data-structure
# Runtime: 8578 ms

class AllOne:

    def __init__(self):
        self.counts = {}
        self.keys = []
        self.keySet = set()

    def inc(self, key: str) -> None:
        self.counts[key] = self.counts.get(key, 0) + 1
        if key not in self.keySet:
            self.keys.append(key)
            self.keySet.add(key)
        self.keys.sort(key = lambda x : self.counts[x])

    def dec(self, key: str) -> None:
        if key not in self.counts:
            return
        
        self.counts[key] -= 1
        curr = self.counts[key]

        if curr == 0:
            self.keys.remove(key)
            self.keySet.remove(key)
        self.keys.sort(key = lambda x : self.counts[x])

    def getMaxKey(self) -> str:
        if len(self.keys) == 0:
            return ""
        return self.keys[-1]

    def getMinKey(self) -> str:
        if len(self.keys) == 0:
            return ""
        return self.keys[0]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()