class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        isFirst = True
        count = 0
        preNum = -1
        for x in nums:
            if isFirst == True:
                nums[count] = x
                preNum = x
                count += 1
                isFirst = False
            else:
                if x != preNum:
                    nums[count] = x
                    count += 1
                    preNum = x
        return count
