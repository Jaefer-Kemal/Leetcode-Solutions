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
        emp_info = defaultdict(list)
        root = None
        for employee in employees:
            if employee.id == id:
                root = employee.id

            emp_info[employee.id] = employee
        
        if not root:
            return 0

        queue = deque([root])
        total_importance = 0

        while queue:
            emp_id = queue.popleft()
            emp = emp_info[emp_id]

            total_importance += emp.importance

            for sub in emp.subordinates:
                queue.append(sub)

        return total_importance


