class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop() 
                answer[idx] = i - idx
            stack.append((temperatures[i], i))
            
        return answer