class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        divider = len(piles)//3
        sorted = [piles[i:i+divider] for i in range(0,len(piles),divider)]
        sorted = sorted[1:]
        piles.clear()
        sum = 0
        for arr in sorted:
            for i in arr:
                piles.append(i)

        for i in range(0, len(piles), 2):
            sum += piles[i] 

        return sum