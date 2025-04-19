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
        employee_map = defaultdict(list)
        target_id = None
        
        for employee in employees:
            if employee.id == id:
                target_id = employee.id

            employee_map[employee.id] = employee
        
        if not target_id:
            return 0

        queue = deque([target_id])
        total_importance = 0

        while queue:
            current_id = queue.popleft()
            current_employee = employee_map[current_id]

            total_importance += current_employee.importance

            for sub in current_employee.subordinates:
                queue.append(sub)

        return total_importance


