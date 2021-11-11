# 342

'''
  This is kind of a cheat but does provide what the question asks. 
  Get the powers of 4 before hand and check if input in set.
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n in set(list([1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]))