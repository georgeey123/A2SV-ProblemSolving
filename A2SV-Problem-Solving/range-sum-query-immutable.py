class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.prefix_sum = [0] * (N+1)
        for i in range(1,N+1):
            # if i == 0:
            #     self.prefix_sum[i] = nums[i]
            # else: 
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]
            # print(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.prefix_sum[right + 1]
        leftsum = self.prefix_sum[left] #if left > 0 else 0

        return rightsum - leftsum





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)