class Solution:
    def climbStairs(self, n: int) -> int:
        prev = {}
        prev[1] = 1
        prev[2] = 2

        for idx in range(3, n + 1):
            prev[idx] = prev[idx-1] + prev[idx - 2]

        return prev[n]


print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))
print(Solution().climbStairs(7))
print(Solution().climbStairs(500))
