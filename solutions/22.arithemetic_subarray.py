class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        query = 0
        temp = []
        answer = [None for _ in range(len(l))]
        while query <= len(l) - 1:
            temp = nums[l[query]: r[query] + 1]
            temp.sort()
            
            for num in range(len(temp)-1):
                if(temp[num + 1] - temp[num] == temp[1] - temp[0]):
                    answer[query] = True
                else:
                    answer[query] = False

            query += 1
        return answer 