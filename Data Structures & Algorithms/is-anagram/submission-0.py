class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [i for i in s ] 
        b = [j for j in t]
       
        return sorted(a) == sorted(b)