# Problem: https://leetcode.com/problems/binary-watch
# Runtime: 0 ms

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def numActive(number):
            out = 0
            for i in range(6):
                if number & (1 << i):
                    out += 1
            return out
        

        hourOptions = {i : [] for i in range(5)}
        minuteOptions = {i : [] for i in range(7)}
        for i in range(64):
            active = numActive(i)
            if i < 12:
                hourOptions[active].append(i)
            if i < 60:
                minuteOptions[active].append(i)

        out = []
        for hourBits in range(min(turnedOn + 1, 5)):
            minuteBits = turnedOn - hourBits

            for hourNum in hourOptions.get(hourBits, []):
                for minuteNum in minuteOptions.get(minuteBits, []):
                    out.append(f"{hourNum}:{minuteNum:02d}")
        return out