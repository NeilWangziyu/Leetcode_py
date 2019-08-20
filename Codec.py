class Codec:
    dict = {}
    index = 0
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        self.index += 1
        self.dict["https://tinyurl.com/" + str(self.index)] = longUrl
        return "https://tinyurl.com/" + str(self.index)





    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.dict[shortUrl]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))