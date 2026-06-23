# Problem: https://leetcode.com/problems/validate-ip-address
# Runtime: 0 ms

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return 'IPv4'
        elif self.isIPv6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'
    
    def isIPv4(self, ip):
        parts = ip.split(".")

        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isnumeric() or (part != '0' and part[0] == '0'):
                return False
            if int(part) < 0 or int(part) > 255:
                return False
        
        return True
    
    def isIPv6(self, ip):
        parts = ip.split(':')

        if len(parts) != 8:
            return False

        for part in parts:
            if len(part) == 0 or len(part) > 4:
                return False
            for c in part:
                valid = c.isnumeric() or ord('a') <= ord(c.lower()) <= ord('f')
                if not valid:
                    return False
        
        return True