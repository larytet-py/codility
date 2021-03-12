# codility

Some losely relevant notes

```
import unittest


def solution_a(A):
    A.sort()
    if len(A) == 0:
        return 1
    last_v = A[0]
    print(A)
    for v in A:
      if last_v < 0:
        last_v = v
        continue
      if (v - last_v) > 1:
          return min(v+1, last_v+1)
      last_v = v
    return max(1, v+1)


class TestSolutionA(unittest.TestCase):

  # Use code to generate random integer list. 
  # random.sample(range(-1000000, 1000000), 10)

    def test_case0(self):
      input_list = [1, 3, 6, 4, 1, 2]
      val = solution_a(input_list)
      self.assertEqual(val, 5)

    def test_case1(self):
      input_list = [1, 2, 3]
      val = solution_a(input_list)
      self.assertEqual(val, 4)

    def test_case2(self):
      input_list = [ -1, -3]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case3(self):
      input_list = [100000, 500, 10]
      val = solution_a(input_list)
      self.assertEqual(val, 11)

    def test_case4(self):
      input_list = [ -5, -10, -2, 0]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case5(self):
      input_list = [ -5, -10, -2, 0]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case6(self):
      input_list = [-266959, -559850, 667410, -370471, -695927, 170911, 658702, -737673, 370182, -285767]
      val = solution_a(input_list)
      self.assertEqual(val, 170912)

    def test_case7(self):
      input_list = [860108, 591722, -969778, -439377, -511718,\
 -207087, -457298, 908118, 311622, 519103, -975605, -157567,\
 -318617, -634176, 264219, -82032, -277682, -364746, -788141,\
 584287]
      val = solution_a(input_list)
      self.assertEqual(val, 264220)


# http://leetcodejavasol.blogspot.com/2018/02/maximum-squared-distance.html
def solution_b(A, B, C, D):
    # write your code in Python 3.6
    distances = []
    distances.append((A-B)*(A-B) + (C-D)*(C-D))
    distances.append((A-C)*(A-C) + (B-D)*(B-D))
    distances.append((A-D)*(A-D) + (B-C)*(B-C))
    distances.sort()
    return distances[2]

    def test_case0(self):
      val = solution_b(1,1,2,2)
      self.assertEqual(val, 5)


# https://www.geeksforgeeks.org/minimum-increment-operations-to-make-array-unique/


# function to find minimum increment required
# Python3 Implementation of above approach
import collections
 
# function to find minimum increment required
def solution_c(A):
    count = collections.Counter(A)
    taken = []
    ans = 0
 
    for x in range(100000):
        if count[x] >= 2:
            taken.extend([x] * (count[x] - 1))
        elif taken and count[x] == 0:
            ans += x - taken.pop()
    return ans
 
def solution_d(A):
    # write your code in Python 3.6
    result = 0
    unique_values = []
    # https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
    number_of_appearances = collections.Counter(A)
 
    for val in range(200000):
        if number_of_appearances[val] > 1:
            count = (number_of_appearances[val] - 1)
            for _ in range(count):
              unique_values.append(val)
        elif unique_values and number_of_appearances[val] == 0:
            result += val - unique_values.pop()
 
    return result

def solution_e(A):
    # write your code in Python 3.6
    # write your code in Python 3.6
    result = 0
    if len(A) < 2:
      return 0

    A.sort()
    last_v = A[0]
    for val in A[1:0]:
      if 
 
    return result

class TestSolutionC(unittest.TestCase):
  def test_case0(self):
    val = solution_d( [6, 2, 3, 5, 6, 3])
    self.assertEqual(val, 2)


```  

http://bit.ly/owb-logs-2019
