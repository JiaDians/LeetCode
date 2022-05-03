class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sum = 0
        mapping = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < len(s):
            if s[i] == 'I' or s[i] == 'X' or s[i] == 'C':
                if i+1 < len(s):
                    if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X') \
                        or s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C') \
                            or s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                        sum += mapping[s[i+1]] - mapping[s[i]]
                        i += 1
                    else:
                        sum += mapping[s[i]]
                else:
                    sum += mapping[s[i]]
            else:
                sum += mapping[s[i]]
            i += 1
        return sum
