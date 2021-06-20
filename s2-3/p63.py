import numpy as np

class Bubunretu():
    def __init__(self, a):
        self.a = a
        self.n = self.a.shape[0]
        self.dp = np.full(self.n, 1, dtype=np.int32)
    def solve(self):
        maxlen = 0
        for i in range(1, self.n):
            for j in range(i):
                if(self.a[j] < self.a[i]):
                    self.dp[i] = max(self.dp[i], self.dp[j] + 1)
                    if(self.dp[i] > maxlen):
                        maxlen = self.dp[i]
        print(maxlen)
        


if __name__ == '__main__':
    a = np.array([4, 2, 3, 1, 5])
    bubunretu = Bubunretu(a)
    bubunretu.solve()
    