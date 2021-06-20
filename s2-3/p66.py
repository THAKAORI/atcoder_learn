import numpy as np

class Bunkatu():
    def __init__(self, n, m, M):
        self.n = n
        self.m = m
        self.M = M
        self.dp = np.zeros((self.m+1, self.n+1), dtype=np.int32)
    
    def solve(self):
        self.dp[0, 0] = 1
        for i in range(1, self.m+1):
            for j in range(self.n+1):
                if(j - i >= 0):
                    self.dp[i, j] = self.dp[i-1, j] + self.dp[i, j-i]
                else:
                    self.dp[i, j] = self.dp[i-1, j]
        print(self.dp)


if __name__ == '__main__':
    n = 4
    m = 3
    M = 10000
    bunkatu = Bunkatu(n, m, M)
    bunkatu.solve()
