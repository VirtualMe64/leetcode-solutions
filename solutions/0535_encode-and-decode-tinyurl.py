# Problem: https://leetcode.com/problems/encode-and-decode-tinyurl
# Runtime: 42 ms

class Codec:
    def __init__(self):
        self.longToShort = {}
        self.shortToLong = {}
        self.index = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        shortUrl = f"tinyurl.com/{self.index}"
        self.shortToLong[self.index] = longUrl
        self.index += 1
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = int(shortUrl[12:])
        if key in self.shortToLong:
            return self.shortToLong[key]
        return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))