class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        distance = []
        
        for i in range(len(position)):
            stack.append((position[i], speed[i]))

        stack.sort(reverse=True)

        for (p, s) in stack:
            d = (target - p) / s
            distance.append(d) 
            if len(distance) >=2 and distance[-1] <= distance[-2]:
                distance.pop()

        return len(distance)