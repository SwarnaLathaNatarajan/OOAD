class Strategy:
    def multiply(self,a,b): pass

class StrategyA(Strategy):
    def multiply(self,a,b):
        return a*b

class StrategyB(Strategy):
    def multiply(self,a,b):
        ans = 0
        for i in range(b):
            ans+=a
        return ans

class Calculator:
    def __init__(self,strategy=StrategyA()):
        self.strategy = strategy

    def multiple(self,a,b):
        return self.strategy.multiply(a,b)

if __name__ == '__main__':
    calc1 = Calculator()
    calc2 = Calculator(StrategyB())
    print(calc1.multiple(7,8),calc2.multiple(7,8))
