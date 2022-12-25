class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = []

        for i in tasks:
            if i not in counts:
                counts.append(i)

        reps = [tasks.count(i) for i in counts]
        reps.sort()
        
        mostRepeated = reps.pop()
        freeSpace = mostRepeated - 1
        idle = freeSpace * n

        while len(reps) > 0 and idle > 0:
            idle -= min(freeSpace, reps.pop())
            
        return max(0, idle) + len(tasks)