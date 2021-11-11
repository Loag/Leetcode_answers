# 1198

from collections import defaultdict
from types import List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cont = defaultdict(set)
        for index, row in enumerate(mat):
            for val in row:
                cont[val].add(index)
        
        for k in sorted(list(cont.keys())):
            if len(cont[k]) == len(mat):
                return k
        return -1