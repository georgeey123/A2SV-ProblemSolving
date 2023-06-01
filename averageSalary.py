class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = max(salary)
        min_sal = min(salary)
        sum = 0
        avg_sal = 0
        
        for i in range(len(salary)):
            sum += salary[i]

        avg_sal = (sum - max_sal - min_sal) / (len(salary) - 2)

        return avg_sal
            
