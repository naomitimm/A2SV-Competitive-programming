# def dailyTemp(temperatures):
#     answer = []
#     found = False

#     for temp in range(len(temperatures)):
#         if temp < len(temperatures) - 1:
#             if temperatures[temp] < temperatures[temp + 1]:
#                 answer.append(1)

#             elif(temperatures[temp] >= temperatures[temp + 1]):
#                 sub = temperatures[temp + 1:]
#                 for i in range(len(sub)):
#                     if sub[i] > sub[0]:
#                         answer.append(i)
#                         found = True
#                         break
#                 if found == False:
#                     answer.append(0)

#             found = False

#         elif temp == len(temperatures) - 1:
#             answer.append(0)
#             break
                   
#     return answer

# dailyTemp([73,74,75,71,69,72,76,73])

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in temperatures]
        stack = []
        for i in range(len(temperatures)):
            while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            
        return answer

