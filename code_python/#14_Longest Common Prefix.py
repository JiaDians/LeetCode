class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strMinLen = 200
        matchStr = ''
        isDifferent = False
        isFirstStr = True
        for str in strs:
            strMinLen = min(strMinLen, len(str))

        for i in range(strMinLen):
            isDifferent = False
            isFirstStr = True
            matchChar = ''
            for str in strs:
                if isFirstStr == True:
                    matchChar = str[i]
                    isFirstStr = False
                else:
                    if str[i] != matchChar:
                        isDifferent = True
                        break
            if isDifferent == True:
                break
            else:
                matchStr += matchChar

        return matchStr
