
def discrete_factor(category):
    factor = {'+': 1.2,
              '++': 1.4,
              '+++': 1.8,
              0: 1,
              '-': -1.2,
              '--': -1.4,
              '---': -1.8}

    assert category in factor.keys()

    def f(argument):
        return factor[category] * argument

    return f
    

def square():
    def f(argument):
        return argument * argument
    return f
