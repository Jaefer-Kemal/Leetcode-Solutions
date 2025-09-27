class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = defaultdict(list)
        res = []

        for index, group in enumerate(groupSizes):
            group_map[group].append(index)
        
        for group, values in group_map.items():
            grouped = []
            for value in values:
                grouped.append(value)
                if len(grouped) >= group:
                    res.append(grouped)
                    grouped = []
            
            if grouped:
                res.append(grouped)
        
        return res

 


