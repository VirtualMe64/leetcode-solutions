# Problem: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero
# Runtime: 277 ms

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        cnt = 0
        for n in nums:
            stackTop = stack[-1] if len(stack) > 0 else -1
            if n > stackTop:
                stack.append(n)
            else:
                while len(stack) > 0 and stackTop > n:
                    oldTop = stack.pop(-1)
                    if oldTop != 0:
                        cnt += 1
                    stackTop = stack[-1] if len(stack) > 0 else -1
                
                if stackTop != n:
                    stack.append(n)

        for n in stack:
            if n != 0:
                cnt += 1

        return cnt