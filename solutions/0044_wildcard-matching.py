# Problem: https://leetcode.com/problems/wildcard-matching
# Runtime: 39 ms

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # hard part is * -- how to know how long to make it
        # idea 1: be greedy (take 0) and backtrack to last star if error

        # preprocessing: get rid of any consecutive stars
        p2 = ""
        last = ""
        for c in p:
            if c != "*" or last != "*":
                p2 += c
            last = c

        s_ptr = 0
        p_ptr = 0
        star_stack = []
        # (p_ptr, s_ptr, star length)
        while s_ptr < len(s):
            s_char = s[s_ptr]
            p_char = p2[p_ptr] if p_ptr < len(p2) else ""

            if p_char == '?' or s_char == p_char:
                # default case: match or wildcard
                s_ptr += 1
                p_ptr += 1
            elif p_char == '*':
                # fancy case: star
                if p_ptr == len(p2) - 1:
                    return True
                star_stack = [(p_ptr, s_ptr, 0)]
                p_ptr += 1
            else:
                # no match, if no star we're done
                while len(star_stack) > 0:
                    star = star_stack.pop()
                    if star[1] + star[2] + 1 >= len(s):
                        # this star has exceeded max length
                        continue
                    star_stack.append((star[0], star[1], star[2] + 1))
                    p_ptr = star[0] + 1
                    s_ptr = star[1] + star[2] + 1
                    break
                else:
                    return False
        
        # for case where pattern ends early
        return p_ptr >= len(p2) or (p_ptr == len(p2) - 1 and p2[p_ptr] == "*")