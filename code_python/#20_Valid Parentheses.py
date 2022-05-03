class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['(', '{', '[']
        b = [')', '}', ']']
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for x in s:
            if x in b:
                if mapping[x] not in stack:
                    return False
                d = stack.pop()
                if d == mapping[x]:
                    continue
                else:
                    return False
            elif x in a:
                stack.append(x)
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
