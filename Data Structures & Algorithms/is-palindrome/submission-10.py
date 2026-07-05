class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) -1
        

        while start < end:
            
            while not s[start].isalnum() and start < len(s)-1:
                start += 1
            while not s[end].isalnum() and end > 0:
                end -= 1
            
            print(s[start], s[end])
            if start > end:
                break
            if s[start].casefold() != s[end].casefold():
                return False
            
            print(start, end)
            start +=1
            end -= 1
        return True

        #ss__s_s__