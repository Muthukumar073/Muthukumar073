class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return[i,j]
        return[]    

solution=Solution()
nums=[2,6,1,5]
target=7
print(solution.twoSum(nums,target))