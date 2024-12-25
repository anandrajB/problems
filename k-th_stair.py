from functools import cache
# no of ways to reach the k-th stair

class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def rec(stair,jump,used):
            val= stair == k
            if stair>k+1: return 0
            if used:
                return val+rec(stair+2**jump,jump+1,0)
            return val+rec(stair-1,jump,1)+rec(stair+2**jump,jump+1,0)
        return rec(1,0,0)
        
                
            