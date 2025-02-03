from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        for i in nums:
            root = trie
            for j in format(i,'032b'):
                if j not in root:
                    root[j] = {}
                root = root[j]
            root['val'] = i
        res = 0
        for i in nums:
            root = trie
            for j in format(i,'032b'):
                comp = str(int(j)^1)
                if comp in root:
                    root = root[comp]
                elif j in root:
                    root = root[j]
            res = max(res, i^root['val'])

        return res