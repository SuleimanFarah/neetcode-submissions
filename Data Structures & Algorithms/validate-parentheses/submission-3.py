class Solution:
    def isValid(self, s: str) -> bool:
        o = []
        i = 0
        while i < len(s):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                o.append(s[i])
            elif s[i] == "]" or s[i] == "}" or s[i] == ")":
                if len(o) == 0:
                    return False
                value = o.pop()
                if (s[i] == "]" and value != "[") or (s[i] == "}" and value != "{") or (s[i] == ")" and value != "("):
                    return False
            i +=1
        
        if len(o) > 0:
            return False
        return True
