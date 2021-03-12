import unittest

def solution_f(A):
  A.sort()
  last_v = A[0]
  result = 0
  for v in A[1:]:
    if last_v == v:
      diff = 1
      result += diff
      last_v = v + diff
    elif last_v < (v-1):
      diff = v - last_v - 1
      result += diff
      last_v = v + diff
    else:
      last_v = v

  return result


class TestSolutionF(unittest.TestCase):
  def test_case0(self):
    val = solution_f( [1,2,1])
    self.assertEqual(val, 2)

  def test_case1(self):
    val = solution_f( [2,1,4,4])
    self.assertEqual(val, 1)

  def test_case2(self):
    val = solution_f( [6,2,3,5,6,3])
    self.assertEqual(val, 4)
