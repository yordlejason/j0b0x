from Trie import Trie
import urllib3

# Import English Dictionary
http = urllib3.PoolManager()
url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
response = http.request('GET', url)
raw_data = response.data.decode('utf-8')

# Parse
parser = lambda raw: raw.split('\r\n')
parsed = parser(raw_data)

# Insert words in the Trie
db = Trie()
while parsed:
    db.insert(parsed.pop())
