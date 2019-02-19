
def discrete_factor(category):
    factor = {'+': 0.5,
              '++': 0.15,
              '+++': 0.45,
              0: 0,
              '-': -0.5,
              '--': -0.15,
              '---': -0.45}

    assert category in factor.keys()

    def f(delta, curr_value):
        if delta * factor[category] > 0:
            return factor[category] * (100-curr_value) * delta / 100
        else:
            return factor[category] * (curr_value) * delta / 100

    return f


def square():
    def f(argument):
        return argument * argument
    return f
