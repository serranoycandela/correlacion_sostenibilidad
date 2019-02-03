from value_functions import discrete_factor as f
from value_functions import square as g
from model import CriteriaVector

matrix_list = [
  [None,     f('---'),  f('--'),  f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  [f('---'), None,      f('--'),  f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   None,     f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   None,   f(0),   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   None,   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), None,    f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), f('++'), None,     f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), f('++'), f('+++'), None],
]


def test_update_with_list():
    v = CriteriaVector([1, 1, 1, 1, 1, 1, 1, 1],
                       matrix_list)

    v.update(0, delta=1)

    assert v.variables == [2, 1.2, 1.6, 1.8, 2, 2.2, 2.4, 2.8]


matrix_dict = {
  'key0':
  [None,     f('---'),  f('--'),  f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  'key1':
  [f('---'), None,      f('--'),  f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  'key2':
  [f('---'), f('--'),   None,     f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  'key3':
  [f('---'), f('--'),   f('-'),   None,   f(0),   f('+'),  f('++'),  f('+++')],
  'key4':
  [f('---'), f('--'),   f('-'),   f(0),   None,   f('+'),  f('++'),  f('+++')],
  'key5':
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), None,    f('++'),  f('+++')],
  'key6':
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), f('++'), None,     f('+++')],
  'key7':
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), f('++'), f('+++'), None],
}


def test_update_with_dict():
    v = CriteriaVector([1, 1, 1, 1, 1, 1, 1, 1],
                       matrix_dict)

    v.update('key7', delta=1)

    assert v.variables == [1.2, 1.6, 1.8, 2, 2.2, 2.4, 2.8, 2]


mixed_func_matrix = [
  [None,     f('---'),  f('--'),  f('-'), f(0),   f('+'),  f('++'),  f('+++')],

  # suddenly wild value function appears!
  [g(),      None,      g(),      g(),    g(),    g(),     g(),      g()],

  [f('---'), f('--'),   None,     f('-'), f(0),   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   None,   f(0),   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   None,   f('+'),  f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), None,    f('++'),  f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), f('++'), None,     f('+++')],
  [f('---'), f('--'),   f('-'),   f(0),   f('+'), f('++'), f('+++'), None],
]


def test_update_with_other_value_function():
    v = CriteriaVector([1, 1, 1, 1, 1, 1, 1, 1],
                       mixed_func_matrix)

    v.update(1, delta=2)

    assert v.variables == [5, 3, 5, 5, 5, 5, 5, 5]
