# 1877
'''
  this implementation is very slow ~5% on speed
  but pretty good on space ~99%
'''
from types import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort nums
        nums.sort()
        # create set to hold vals, we don't care about duplicates
        vals = set()
        # iterate nums
        while nums:
            # add pair sum to set
            vals.add(nums.pop(0) + nums.pop())
        
        # return max in set
        return max(vals)