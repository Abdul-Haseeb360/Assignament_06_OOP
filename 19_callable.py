
class Multiplier():
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

multiplier = Multiplier(10)

print(multiplier(2))
print(callable(multiplier))

