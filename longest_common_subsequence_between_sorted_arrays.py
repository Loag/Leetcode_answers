from collections import defaultdict
from types import List

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        cont = defaultdict(set)
        
        for index, num_list in enumerate(arrays):
            for val in num_list:
                cont[val].add(index)
        
        res = []
        check_len = len(arrays)
        
        for key in cont.keys():
            if len(cont[key]) == check_len:
                res.append(key)
                
        return res