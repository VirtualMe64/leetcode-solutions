# Problem: https://leetcode.com/problems/simplify-path
# Runtime: 20 ms

class Solution:
    def simplifyPath(self, path: str) -> str:
        path.replace(r"/+", "/")
        parts = path.split("/")
        out = []

        idx = 0
        for part in parts:
            if part == '.':
                continue
            if part == '..':
                idx = idx - 1 if idx > 0 else 0
            elif len(part) > 0:
                if len(out) == idx:
                    out.append(part)
                    idx += 1
                else:
                    out[idx] = part
                    idx += 1
        
        return "/" + "/".join(out[0:idx])