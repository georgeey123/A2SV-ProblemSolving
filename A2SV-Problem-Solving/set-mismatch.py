class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [] 

        i = 0
        while i < n:
            if nums[i]-1 != i:
                if nums[i] == nums[nums[i]-1]:
                    ans.append(nums[i])
                    ans.append(i+1)
                    i+=1
                else:
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        
        return ans[-2:]