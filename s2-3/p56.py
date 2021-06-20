import numpy as np

class MostLong():
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.dp = np.zeros((len(self.s)+1, len(self.t)+1), dtype=np.int32)
        self.n = len(s)
        self.m = len(t)

    def solve(self):
        for i in range(self.n):
            for j in range(self.m):
                if(self.s[i] == self.t[j]):
                    self.dp[i+1, j+1] = self.dp[i, j] + 1
                else:
                    self.dp[i+1, j+1] = max(self.dp[i, j+1], self.dp[i+1, j])
        
        print(self.dp[self.n, self.m])
        print(self.dp)

if __name__ == '__main__':
    s = "abcd"
    t = "becd"
    mostlong = MostLong(s, t)
    mostlong.solve()
