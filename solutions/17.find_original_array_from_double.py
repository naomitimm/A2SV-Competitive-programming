class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        first = changed[:(len(changed)//2)]
        second = changed[(len(changed)//2):]

        for i in range(len(first)):
            if first[i] == (second[i])//2:
                changed.pop()
        
        if len(changed) == len(first):
            return changed
        else :
            return []