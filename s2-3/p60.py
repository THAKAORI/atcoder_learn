import numpy as np

class Napzac():
    def __init__(self, goods, maxW):
        self.goods = goods
        self.maxW = maxW
        self.n = goods.shape[0]
        self.dp = np.zeros((self.n+1, self.maxW+1), dtype=np.int32)

    def solve1(self):
        for i in range(self.n):
            for j in range(self.maxW+1):
                if(j < self.goods[i, 0]):
                    self.dp[i+1, j] = self.dp[i, j]
                else:
                    self.dp[i+1, j] = max(self.dp[i, j], self.dp[i+1, j - self.goods[i, 0]] + self.goods[i, 1])
        print(self.dp[self.n, self.maxW])
        print(self.dp)

if __name__ == '__main__':
    goods = np.array([[2, 3], [1, 2], [3, 4], [2, 2]])
    maxW = 5
    napzac = Napzac(goods, maxW)
    napzac.solve1()