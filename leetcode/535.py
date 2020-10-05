import random

class Codec:
    def __init__(self):
        self.db = {}
    
    def get_short_url(self):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        tiny_url = ''
        
        for _ in range(6):
            tiny_url += random.choice(chars)
            
        while tiny_url in self.db:
            tiny_url = get_short_url()
        return tiny_url
            
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tiny_url = self.get_short_url()
        self.db[tiny_url] = longUrl
        
        return tiny_url
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))