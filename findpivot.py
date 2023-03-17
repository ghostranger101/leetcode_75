class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            if sum(nums[:i])==sum(nums[i+1:len(nums)]):
                ans=i
                break
            else:ans=-1
        return ans
