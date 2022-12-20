class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        counter = 0
        unique = []

        for number in nums:
            if (number not in unique):
                counter += 1
                unique.append(number)

        counts = [[] for _ in range(counter)] 

        for u in range(len(unique)):
            for num in nums:
                if unique[u] == num:
                    counts[u].append(num)


        length = [len(i) for i in counts]
        result = []
        
        while k>0:
            maximum = max(length)
            result.append((length.index(maximum)))
            length[length.index(maximum)] = 0 
            k -= 1

        unique.clear()

        for j in result:
            unique.append((counts[j][0]))

        return unique 