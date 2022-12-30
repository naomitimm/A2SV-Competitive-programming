class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        stack = []
    
        for i in range(len(nums)):
            temp = nums[i:]
            diff = max(temp) - min(temp)
            if diff <= limit:
                stack.append(len(temp))


        return max(stack)