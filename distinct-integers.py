'''
N integers in array of [1..N] In one move you inc/dec the value by 1
After every move all number should remain within [1..N]
What is the smallest number of steps to make all values distinct?
[1,2,1] can be changed in 2 steps [1,2,2], [1,2,3]
[6,2,3,5,6,3] 4 steps [6,2,1,5,3]
'''

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
