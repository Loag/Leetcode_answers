from types import List

'''
70. Climbing Stairs. & 509. Fibonacci Number
for 509 just have to change if i < 3: to i < 2:
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        cont = {}
        
        def dp(i):
            if i < 3:
                return i
            
            if i not in cont:
                # it equals all the ways to get there from one or two steps behind
                cont[i] = dp(i - 1) + dp(i - 2)  
            return cont[i]
        
        return dp(n)

# 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cont = {}

        def dp(i):
            # we get to start at 0 or 1 so it can be treated as zero
            if i < 2: 
                return 0
            
            # if i (the current position) is not in the cache dict
            if i not in cont:
                
                # this is the cost of getting to this position
                '''
                Get the minimum between:
                    - the return of the dp function for the prev pos + the cost of the prev pos
                    - the return of the dp function for the prev prev pos + the cost of the prev prev pos
                    
                This is how we know which move to make
                '''
                cont[i] = min(dp(i - 1)  + cost[i - 1], dp(i - 2) + cost[i - 2]) # Recurrence relation
            
            # return the cost of getting to this pos
            return cont[i]
        
        return dp(len(cost))

# 1137. N-th Tribonacci Number 
class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i < 2:
                return 0
            if i == 2:
                return 1
            if i not in cont:
                cont[i] = dp(i-1) + dp(i - 2) + dp(i - 3)
            return cont[i]
        
        cont = {}
        return dp(n+1)