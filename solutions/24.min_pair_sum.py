class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        pairs = []
        result = 0
        
        for i in range(len(nums)):
            pairs.append((nums[i] + nums[len(nums)-(1+i)]))
            
        pairs = pairs[:(len(pairs)//2)]
        result += max(pairs) 

       
        return result