class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictM = {}
        for word in strs :
            key =  "".join(sorted(word))
            if key in dictM :
                dictM[key].append(word)
            else:
                dictM[key] = [word]
        return list(dictM.values())