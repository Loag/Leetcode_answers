# 1198

from collections import defaultdict
from types import List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # new default dict with set as default
        cont = defaultdict(set)
        # iterate over rows w/ index
        for index, row in enumerate(mat):
            # iterate over values in the row
            for val in row:
                # for the value, add the row index
                cont[val].add(index)
        
        # iterate over dict keys in order
        for k in sorted(list(cont.keys())):
            '''
              because the values are unique, if the 
              length of the set of values is the same
              as the length of rows, we know that the 
              value is in each row. Because ordered
              we will find the smallest first.
            '''
            if len(cont[k]) == len(mat):
                return k
        
        # if not default to return -1
        return -1