import numpy as np

class Tyouhuku():
    def __init__(self, a, m, M):
        self.a = a
        self.n = self.a.shape[0]
        self.m = m
        self.M = M
        self.dp = np.zeros((self.n+1, self.m+1), dtype=np.int32)

    def solve(self):
        for i in range(self.n+1):
            self.dp[i, 0] = 1
        for i in range(1, self.n+1):
            for j in range(1,self.m+1):
                if(j - 1 - self.a[i-1] >= 0):
                    self.dp[i, j] = self.dp[i-1, j] + self.dp[i, j-1] - self.dp[i-1, j-1-self.a[i-1]]
                else:
                    self.dp[i, j] = self.dp[i-1, j] + self.dp[i, j-1]
        
        print(self.dp)
    def solve2(self):
        for i in range(self.n+1):
            self.dp[i, 0] = 1
        for i in range(self.n):
            for j in range(1, self.m+1):
                if(j - 1 - self.a[i] >= 0):
                    self.dp[i+1, j] = self.dp[i+1, j-1] + self.dp[i, j] - self.dp[i, j-1-self.a[i]]
                else:
                    self.dp[i+1, j] = self.dp[i+1, j-1] + self.dp[i, j]
        print(self.dp)

if __name__ == '__main__':
    a = np.array([1, 2, 3])
    m = 3
    M = 10000
    tyouhuku = Tyouhuku(a, m, M)
    tyouhuku.solve()
