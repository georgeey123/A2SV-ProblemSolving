class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = ""

        for c in path + "/":
            if c == "/":
                if temp == "..":
                    if stack: stack.pop()
                elif temp != "" and temp != ".":
                    stack.append(temp)
                temp = ""
            else:
                temp += c

        return "/" + "/".join(stack)