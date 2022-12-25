class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []

        for num in nums1:
            index = nums2.index(num)
            temp = nums2[index:]
            if len(temp) == 1:
                result.append(-1)
            else:
                for i in temp[1:]:
                    j = temp.index(i)
                    if i > temp[0]:
                        result.append(i)
                        break

                    elif i < temp[0] and j < len(temp) - 1:
                        continue

                    else:
                        result.append(-1)

        while len(result) > len(nums1):
            result.pop()  

        return result