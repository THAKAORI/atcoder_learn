import numpy as np

class FenceRepair():
    def __init__(self, L):
        self.L = L

    def solve(self):
        sorted_cut = np.sort(self.L)[::-1]

        total_cost = 0
        while sorted_cut.size > 1:
            total_cost += np.sum(sorted_cut)
            print(sorted_cut, total_cost)
            sorted_cut = np.delete(sorted_cut, 0)
        
        print(total_cost)

if __name__ == '__main__':
    #L = np.array([8, 5, 8])
    L = np.array([3, 4, 5, 1, 2])
    fencerepair = FenceRepair(L)
    fencerepair.solve()
