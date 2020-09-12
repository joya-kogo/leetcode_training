class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        ans_set = set()
        nums.sort()
        if 4 <= nums.count(0) and target == 0:
            ans_set.add((0,0,0,0))
        print(nums)
        for i in range(len(nums)-2):
            # if nums[i-1] == nums[i]:
            #     continue
            for j in range(i+1, len(nums)-2):
                # if nums[j-1] == nums[j]:
                #     continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    four_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if four_sum == target:
                        ans_set.add((nums[i] , nums[j] , nums[k] , nums[l]))
                        k += 1
                        l -= 1
                        while k < l and ( nums[k] == nums[k-1] ):
                            k += 1
                        while k < l and ( nums[l] == nums[l+1] ):
                            l -= 1
                    elif four_sum < target:
                        k += 1
                    else:
                        l -= 1
        return ans_set
                        
                    