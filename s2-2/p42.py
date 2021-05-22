import numpy as np

class SelectMoney():
    def __init__(self, C, A, price):
        self.C = C
        self.A = A
        self.price = price

        self.C = self.C[::-1]
        self.price = self.price[::-1]
    def solve(self):
        residual = self.A
        coins = 0
        for c, p in zip(self.C, self.price):
            number = np.floor(residual / p)
            if(number > c):
                residual -= p * c
                coins += c
            else:
                residual -= p * number
                coins += number
                
            if(residual == 0):
                break
        
        print("All coins: ", int(coins))

if __name__ == '__main__':
    C = np.array([3, 2, 1, 3, 0, 2])
    price = np.array([1, 5, 10, 50, 100, 500])
    A = 620
    selectmoney = SelectMoney(C, A, price)
    selectmoney.solve()