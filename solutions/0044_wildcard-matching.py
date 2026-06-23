# Problem: https://leetcode.com/problems/wildcard-matching
# Runtime: 5 ms

from collections import deque
import heapq

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matches(a, b):
            # check if a matches b including ?, but not *
            if len(a) != len(b):
                return False

            for i in range(len(a)):
                if a[i] != b[i] and a[i] != '?' and b[i] != '?':
                    return False
            
            return True
        
        if p.count('*') == 0:
            return matches(s, p)
        
        segments = p.split('*')
        segments = [s for s in segments if len(s) > 0]

        if p[0] != '*':
            start = segments[0]
            if not matches(s[:len(start)], start):
                return False
            s = s[len(start):]
            segments = segments[1:]
        if p[-1] != '*':
            end = segments[-1]
            if not matches(s[-len(end):], end):
                return False
            s = s[:-len(end)]
            segments = segments[:-1]

        sIdx = 0
        pIdx = 0
        while pIdx < len(segments):
            currSegment = segments[pIdx]

            if sIdx + len(currSegment) > len(s):
                return False
            
            if matches(currSegment, s[sIdx : sIdx + len(currSegment)]):
                sIdx += len(currSegment)
                pIdx += 1
                continue
            
            sIdx += 1
            continue
        
        return True