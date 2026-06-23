# Problem: https://leetcode.com/problems/trionic-array-ii
# Runtime: 332 ms

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # step 1: classify stretches as "none", "increasing", "decreasing", or "transition"
        # step 2: find max sum of stretches (at either end)
        # step 3: max sum of consecutive INC-DEC-INC stretch

        # suppose a < b < c, to classify the middle of a three stretch:
        classifications = []
        transitionTypes = {}

        for i in range(len(nums)):
            v1 = nums[i - 1] if i > 0 else (nums[i] - (nums[i + 1] - nums[i]))
            v2 = nums[i]
            v3 = nums[i + 1] if i < len(nums) - 1 else (nums[i] + (nums[i] - nums[i - 1]))

            if v1 == v2:
                if v2 == v3:    classifications.append("none")
                elif v2 < v3:   classifications.append("inc")
                else:           classifications.append("dec")
            elif v1 < v2:
                if v2 == v3:    classifications.append("none")
                elif v2 < v3:   classifications.append("inc")
                else:
                    classifications.append("trans")
                    transitionTypes[i] = "inc"
            else: # v1 > v2
                if v2 == v3:    classifications.append("none")
                elif v2 < v3:
                    classifications.append("trans")
                    transitionTypes[i] = "dec"
                else:           classifications.append("dec")
        

        # info about a transition:
        # [connected to previous, previous full sum, previous max end sum, 
        #  connected to next, next max start sum
        #  value, type]

        transitions = []
        connected = False
        currType = "none"
        currSum = None
        currMaxStartSum = None
        currMaxEndSum = None

        for i in range(len(nums)):
            c = classifications[i]
            n = nums[i]

            if c == "none": # end the stretch, can't connect to next
                if len(transitions) > 0 and connected:
                    transitions[-1][3] = False
                    transitions[-1][4] = currMaxStartSum
                connected = False
                currType = "none"
                currSum = None
                currMaxStartSum = None
                currMaxEndSum = None
            elif c == "trans":
                currMaxStartSum = n if currMaxStartSum is None else max(currMaxStartSum, currSum + n)
                if connected:
                    transitions[-1][3] = True
                    transitions[-1][4] = currMaxStartSum
    
                transitions.append([
                    connected, currSum, currMaxEndSum,
                    False, None,
                    n, transitionTypes[i]
                ])
                connected = True
                currType = "trans"
                currSum = None
                currMaxEndSum = n
                currMaxStartSum = None
            elif c == currType or currType == "trans": # continuing stretch or starting immediately after transition
                currSum = n if currSum is None else currSum + n
                currMaxStartSum = n if currMaxStartSum is None else max(currMaxStartSum, currSum)
                currMaxEndSum = n if currMaxEndSum is None else max(n, currMaxEndSum + n)
                currType = c
            else:
                if len(transitions) > 0:
                    transitions[-1][3] = False
                    transitions[-1][4] = currMaxStartSum

                connected = False
                currType = c
                currSum = n
                currMaxStartSum = n
                currMaxEndSum = n

        if connected:
            transitions[-1][3] = True
            transitions[-1][4] = currMaxStartSum

        # for i in range(len(nums)):
        #     print(nums[i], classifications[i])

        # print(transitions)

        best = None

        for i in range(len(transitions) - 1):
            isTrionic = transitions[i][3] and transitions[i + 1][0] and transitions[i][6] == 'inc'

            if isTrionic:
                # v1 = max end of first stretch
                v1 = transitions[i][5] + (transitions[i][2] if transitions[i][2] is not None else 0)
                # v2 = full sum of middle stretch
                v2 = transitions[i + 1][5] + (transitions[i + 1][1] if transitions[i + 1][1] is not None else 0)
                # v3 = max start of third stretch
                v3 = transitions[i + 1][4] if transitions[i + 1][4] is not None else 0

                # print(i, v1, v2, v3, (v1 + v2 + v3))

                res = v1 + v2 + v3
                best = max(best, res) if best is not None else res
        
        return best