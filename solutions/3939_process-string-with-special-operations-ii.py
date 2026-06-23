# Problem: https://leetcode.com/problems/process-string-with-special-operations-ii
# Runtime: 291 ms

from functools import lru_cache

class Solution:
    def processStr(self, s: str, k: int) -> str:
        # idea 1: backtracking via recursion. works but times out
        # idea 2: first compute length at each index then traverse backwards keeping track of relevant index
        # optimization to idea 2: don't need an explicit state dict
        
        # first get state (length, operation) after east op
        length = 0
        for c in s:
            if c not in "*#%":
                length += 1
            elif c == "*":
                if length > 0:
                    length -= 1
            elif c == "#":
                length *= 2

        # i.e if final string is length 2, any index >= 2 is out of bounds
        if k >= length:
            return '.'

        # scan in reverse until we find an append
        # # and * will change the relevant index
        # removes don't matter since we're scanning in reverse
        curr_index = k
        for c in s[::-1]:
            if c not in "*#%":
                if length - 1 == curr_index:
                    return c
                length -= 1
            elif c == "#":
                # since s is duplicated, we care about the corresponding position from the first half
                length //= 2
                curr_index = curr_index % length
            elif c == "%":
                curr_index = length - curr_index - 1
            else: # c == "*"
                length += 1
        
        # should never happen
        return None