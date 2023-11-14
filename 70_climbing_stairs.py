class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        prev, curr = 1, 1
        for i in range(2, n + 1):
            curr = prev + curr
            prev = curr - prev

        return curr


print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))
print(Solution().climbStairs(7))
print(Solution().climbStairs(500))
