class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffHash = {}
        for ind,val in enumerate(nums) :
            print(diffHash)
            if  val in diffHash :
                return [diffHash[val],ind]
            else:
                diffHash[target - val] = ind
        return [0,0]