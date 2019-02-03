
def discrete_factor(category, argument):
    factor = {'+': 1.2,
              '++': 1.4,
              '+++': 1.8,
              '0': 1,
              '-': 0.8,
              '--': 0.6,
              '---': 0.2}
    
    assert category in factor.keys()

    return argument * factor[category]

    
