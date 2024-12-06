class Solution:
    def simplifyPath(self, path: str) -> str:
        rules = {"..","."}
        ls = deque(path.split("/"))
        res = ["/"]
        while ls:
            print(ls)
            if ls[0] == '':
                ls.popleft()
                continue

            elif ls[0] not in rules:
                res.append(f"{ls.popleft()}/")
            else:
                if ls[0] == ".":
                    ls.popleft()
                    continue
                elif ls[0] == "..":
                    if len(res) != 1:
                        ls.popleft()
                        res.pop()
                    else:
                        ls.popleft()
        if len(res) == 1:
            return "/"
        return "".join(res)[:-1]
                    
        