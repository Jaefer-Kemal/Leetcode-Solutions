class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        stack = []
        for dire in path:
            if (not dire) or dire == ".":
                continue
            if dire == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dire)
        
        return "/" + "/".join(stack)
            
        