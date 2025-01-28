from typing import List

class UnionFind:
    def __init__(self, N):
        self.parent=[i for i in range(N)]
        self.rank=[1 for i in range(N)]
        self.time=0
        self.count=N

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def performUnion(self, u, v, updatedTime):
        if self.count == 1:
            return
 
        rootX = self.find(u)
        rootY = self.find(v)
 
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY
                self.rank[rootY] += 1
            self.time = updatedTime
            self.count -= 1
     
    def getCount(self):
        return self.count
     
    def getTime(self):
        return self.time

def earliestTime(arr: List[List[int]], N: int) -> int:
    arr = sorted(arr, key=lambda x: x[2])
    unionFind = UnionFind(N)
    for it in arr:
        # Function to return current set count
        unionFind.performUnion(it[0], it[1], it[2])
    if unionFind.getCount() == 1:
      # Function to return current time stamp
        return unionFind.getTime()
    else:
        return -1
# Driver Code
if __name__ == "__main__":
    N = 6
    arr = [[0, 1, 4], [3, 4, 5],
           [2, 3, 14], [1, 5, 24],
           [2, 4, 12], [0, 3, 42],
           [1, 2, 41], [4, 5, 11]]
    print(earliestTime(arr, N))