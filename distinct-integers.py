import unittest

def solution_f(A):
  A.sort()
  result = 0
  idx = 1
  for v in A:
    diff = v - idx
    if diff < 0:
      result -= diff
    elif diff > 0:
      result += diff
    idx += 1
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
