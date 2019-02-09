from Trie import Trie
import urllib3


# import English Dictionary
http = urllib3.PoolManager()
url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
response = http.request('GET', url)
raw_data = response.data.decode('utf-8')

# parse raw data
parser = lambda raw: raw.split('\r\n')
parsed = parser(raw_data)

# store words to trie
db = Trie()
while parsed:
    db.insert(parsed.pop())


class Solver:
    def __init__(self, n, grid):
        self._n = n
        self._grid = grid
        self._ret = 0
        self._seen = set()
        self._solve()

    def get_words(self) -> set:
        '''
        Return the set of vaid words found in grid
        '''
        return self._seen.copy()

    def get_number_of_words(self):
        '''
        Return the number of words found in grid
        '''
        return self._ret

    def _solve(self) -> None:
        for row in range(self._n):
            for col in range(self._n):
                self._dfs(row, col)

    def _dfs(self, row: int, col: int, query='', num_char=1) -> None:
        if row >= 0 and row < self._n and col >= 0 and col < self._n and self._grid[row][col] != '#' and db.startswith(query + self._grid[row][col]):
            character = self._grid[row][col]
            query += character
            self._grid[row][col] = '#'
            if num_char > 2 and query not in self._seen and db.search(query):
                self._ret += 1
                self._seen.add(query)
            self._dfs(row+1, col, query, num_char+1)
            self._dfs(row+1, col+1, query, num_char+1)
            self._dfs(row+1, col-1, query, num_char+1)
            self._dfs(row-1, col, query, num_char+1)
            self._dfs(row-1, col+1, query, num_char+1)
            self._dfs(row-1, col-1, query, num_char+1)
            self._dfs(row, col+1, query, num_char+1)
            self._dfs(row, col-1, query, num_char+1)
            self._grid[row][col] = character
