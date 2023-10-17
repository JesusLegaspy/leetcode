from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:

    for index in range(len(digits) - 1, -1, -1):
      if (digits[index] == 9):
        digits[index] = 0
        continue
      digits[index] = digits[index] + 1
      return digits

    return [1] + digits

    ## Second approach
    # result = int("".join([str(digit) for digit in digits])) + 1
    # return [int(digit) for digit in str(result)]


test = Solution()
print(test.plusOne([1,2,3]))
print(test.plusOne([9]))
print(test.plusOne([9,9,9]))