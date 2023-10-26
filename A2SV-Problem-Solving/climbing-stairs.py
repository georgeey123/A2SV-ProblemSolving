class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        def recursiveClimb(n, one, two):
            if n == 0:
                return one
            return recursiveClimb(n - 1, one + two, one)

        return recursiveClimb(n - 2, 2, 1)
