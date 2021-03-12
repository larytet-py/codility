'''
You are given an array A of N integers within the range [1..N] 
In one move, you increase or deccreas the value of any element by 1.
After every move all numbers should remain within the range [1..N]
Your task is to find the smallest required number of moves to make all elements 
in the array pairwise distinct (i.e. no value can appear in the array more than once).

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
