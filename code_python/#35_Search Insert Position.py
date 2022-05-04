class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.findPos(nums, 0, len(nums)-1, target)

    def findPos(self, nums, start, end, target):
        if start > end:
            nums.insert(start, target)
            return start
        mid = start + (end - start) // 2
        if nums[mid] > target:
            return self.findPos(nums, start, mid - 1, target)
        if nums[mid] < target:
            return self.findPos(nums, mid + 1, end, target)
        return mid
