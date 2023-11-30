"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0

        def dfs(employee):
            importance = employee.importance

            for subordinate_id in employee.subordinates:
                subordinate = next(subordinate for subordinate in employees if subordinate.id == subordinate_id)
                importance += dfs(subordinate)

            return importance

        employee = next(employee for employee in employees if employee.id == id)
        return dfs(employee)
