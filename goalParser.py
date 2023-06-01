class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if command[i] == "G":
                result += command[i]
            elif command[i] == "(" and command[i+1] == ")":
                result += "o"
            elif command[i] == "(" and command[i+1] == "a" and command[i+2] == "l":
                result += "al"
            else:
                pass
        return result

            


        
