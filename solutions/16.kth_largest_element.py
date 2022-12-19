# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        sorted = [int(num) for num in nums]
        sorted.sort(reverse=True)
        return(str(sorted[k - 1]))