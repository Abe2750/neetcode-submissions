from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        reverseCounts = {}
        for key in counts:
            if counts[key] in reverseCounts:
                reverseCounts[counts[key]].append(key)
            else:
                reverseCounts[counts[key]] = [key]
        
        reverseKeys = list(sorted(reverseCounts.keys()))[::-1]
        ans = []
        # print(counts)
        # print(reverseCounts)
        # print(reverseKeys)
        i = 0
        l = 0
        while i < k:
            for j in reverseCounts[reverseKeys[l]]:
                print(j)
                ans.append(j)
                i+=1
            l+=1
        return ans