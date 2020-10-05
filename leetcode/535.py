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

"""
* hash
1) 6자리 해시코드를 구한다 (random으로 선택)
2) 충돌이 일어났다면 충돌이 일어나지 않을때까지 1번 과정을 반복한다 (linear probing)
3) hash map에 해시코드를 key, 원래 값을 value로 저장한다
4) 해시코드로 원래 값을 꺼낸다!

실제 short url 알고리즘에서는
DB index -> base62 encoding하여 short url을 구한다
"""