class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)) :
                if i == j :
                    continue
                elif curr == 0 :
                    break
                else:
                    curr*= nums[j]
            ans.append(int(curr))
        return ans