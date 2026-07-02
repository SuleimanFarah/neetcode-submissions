class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedString = []
        #format: number-hashtag-string-..-..-.. repeating
        for strings in strs:
            encodedString.append(str(len(strings)))
            encodedString.append("#") 
            encodedString.append(strings)
        return "".join(encodedString)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j


        return res
      

