#from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        #print(nums, target)
        for idx, item in enumerate(nums):
            if target - item in nums and idx != nums.index(target-item):
                answer.append(idx)
                answer.append(nums.index(target - item))
                break;
        
        return answer


#nums = [3, 2, 6]
#target = 6
#print(Solution.twoSum(nums, target))
