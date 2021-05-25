import numpy as np

class Napzac():
    def __init__(self, weight_value, max_weight):
        self.weight_value = weight_value
        self.max_weight = max_weight
        self.n = self.weight_value.shape[0]

        self.dp = np.full((self.weight_value.shape[0]+1, self.max_weight+1), -1)

    def solve(self):
        print("dp map", self.dp.shape)
        print(self.rec(0, self.max_weight))
    
    def rec(self, i, j):
        print(i, j)
        if(self.dp[i, j] >= 0):
            return self.dp[i, j]

        if(i == self.n):
            res = 0
        elif(j < self.weight_value[i, 0]):
            res = self.rec(i+1, j)
        else:
            res = max(self.rec(i+1, j), self.rec(i+1, int(j-self.weight_value[i, 0])) + self.weight_value[i, 1])
        
        self.dp[i, j] = res
        return res

if __name__ == '__main__':
    weight_value = np.array([[2, 3], [1, 2], [3, 4], [2, 2]], dtype=np.float)
    max_weight = 5
    napzac = Napzac(weight_value, max_weight)
    napzac.solve()
