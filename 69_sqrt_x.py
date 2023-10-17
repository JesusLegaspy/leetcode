import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))


solution = Solution()
print(solution.mySqrt(4))