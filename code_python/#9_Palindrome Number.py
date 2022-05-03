class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        self.inv_x = str_x[::-1]
        return str_x == self.inv_x
