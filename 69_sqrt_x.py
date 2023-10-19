import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # Iterate through squares
        # Once the square is greater than x, the solution is the square - 1.

        # square = 1
        # while True:
        #     if ( x < square * square):
        #         return square - 1
        #     square = square + 1

        ###

        if (x == 0):
            return 0

        def find(lower: int, upper: int):
            if(upper-lower <= 1):
                return lower

            mid = (upper - lower) // 2 + lower
            square = mid * mid
            if (square == x):
                return mid
            if (square < x):
                return find(mid, upper)
            else:
                return find(lower, mid)
        
        return(find(1, x//2 + 1))


print(Solution().mySqrt(1))
print(Solution().mySqrt(4))
print(Solution().mySqrt(9))
print(Solution().mySqrt(16))
print(Solution().mySqrt(64))
print(Solution().mySqrt(63))
print(Solution().mySqrt(1024))
print(Solution().mySqrt(1023))
print(Solution().mySqrt(10000))
print(Solution().mySqrt(9999))

