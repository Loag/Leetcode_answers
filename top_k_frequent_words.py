from collections import defaultdict
from types import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cont = defaultdict(int)
        for w in words:
            cont[w] += 1
        a = sorted(cont.items(), key=lambda x:(-x[1], x[0]))
        return [x for x,y in a[:k]]