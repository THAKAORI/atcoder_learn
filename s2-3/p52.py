import numpy as np

class Napzac():
    def __init__(self, weight_value, max_weight):
        self.weight_value = weight_value
        self.max_weight = max_weight

    def solve(self):
        print(self.weight_value)

if __name__ == '__main__':
    weight_value = np.array([[2, 3], [1, 2], [3, 4], [2, 2]], dtype=np.float)
    max_weight = 5
    napzac = Napzac(weight_value, max_weight)
    napzac.solve()
