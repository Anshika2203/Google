from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        sortedNums=sorted(nums)
        n=len(nums)
        maxXor=0
        l, r=0, 0
        while r<n:
            x=sortedNums[l]
            y=sortedNums[r]
            if y-x>x:
                l+=1
                continue
            for i in range(l, r):
                maxXor=max(maxXor, sortedNums[i]^y)
            r+=1
        return maxXor