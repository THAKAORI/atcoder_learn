import numpy as np

class Bubunwa():
    def __init__(self, a, m, K):
        self.a = a
        self.m = m
        self.n = self.a.shape[0]
        self.K = K
        self.dp = np.full(self.K+1, -1, dtype=np.int32)

    def solve(self):
        self.dp[0] = 0
        for i in range(self.n):
            for j in range(self.K+1):
                if(self.dp[j] >= 0):
                    self.dp[j] = self.m[i]
                elif(j < self.a[i] or self.dp[j - self.a[i]] <= 0):
                    self.dp[j] = -1
                else:
                    self.dp[j] = self.dp[j - self.a[i]] - 1
            print(self.dp)

if __name__ == '__main__':
    a = np.array([3, 5, 8])
    m = np.array([3, 2, 2])
    K = 17
    bubunwa = Bubunwa(a, m, K)
    bubunwa.solve()
