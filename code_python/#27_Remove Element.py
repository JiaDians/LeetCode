class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        for num in nums:
            if num != val:
                nums[pos] = num
                pos += 1
        return pos
