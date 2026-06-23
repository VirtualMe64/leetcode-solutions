# Problem: https://leetcode.com/problems/simplify-path
# Runtime: 0 ms

class Solution:
    def simplifyPath(self, path: str) -> str:
        out = []

        parts = path.split("/")
        idx = 0

        for p in parts:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if idx > 0: idx = idx - 1
            else:
                parts[idx] = p
                idx += 1
        
        return "/" + "/".join(parts[:idx])