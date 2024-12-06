class Solution:
    def simplifyPath(self, path: str) -> str:

        ls = deque(path.split("/"))
        res = []  # Use a simple list to store valid directories
        
        while ls:
            curr = ls.popleft()
            if not curr or curr == ".":  # Ignore empty or '.' segments
                continue
            elif curr == "..":  # Handle parent directory
                if res:  # Pop only if res is not empty
                    res.pop()
            else:
                res.append(curr)  # Add valid directory
        
        # Join the result to form the simplified path
        return "/" + "/".join(res)

    '''First Solution'''
    
        # rules = {"..","."}
        # ls = deque(path.split("/"))
        # res = ["/"]
        # while ls:
        #     print(ls)
        #     if ls[0] == '':
        #         ls.popleft()
        #         continue

        #     elif ls[0] not in rules:
        #         res.append(f"{ls.popleft()}/")
        #     else:
        #         if ls[0] == ".":
        #             ls.popleft()
        #             continue
        #         elif ls[0] == "..":
        #             if len(res) != 1:
        #                 ls.popleft()
        #                 res.pop()
        #             else:
        #                 ls.popleft()
        # if len(res) == 1:
        #     return "/"
        # return "".join(res)[:-1]
                    
        