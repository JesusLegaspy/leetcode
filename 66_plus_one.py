from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    solution = []

    carry = True
    for digit in reversed(digits):
      result = digit
      if carry == True:
        result = result + 1
      if result != 10:
        carry = False
      else:
        solution.insert(0,0)
        continue
      solution.insert(0,result)
    
    if (carry == True):
      solution.insert(0,1)

    return solution

test = Solution()
print(test.plusOne([1,2,3]))
print(test.plusOne([9]))
print(test.plusOne([9,9,9]))