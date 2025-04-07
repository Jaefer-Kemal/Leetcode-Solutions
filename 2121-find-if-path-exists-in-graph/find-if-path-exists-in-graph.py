class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        if len(graph) == 0 or source == destination:
            return True

        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            neighbor = graph[node]

            for dest in neighbor:
                if destination == dest:
                    return True

                if dest not in visited:
                    stack.append(dest)

                visited.add(dest)

        return False



        