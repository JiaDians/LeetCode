class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        f = []
        for i in range(len(needle)):
            if i == 0:
                f.append(-1)
            else:
                temp = f[i-1]
                while True:
                    if needle[temp+1] == needle[i]:
                        f.append(temp+1)
                        break
                    else:
                        if temp == -1:
                            f.append(-1)
                            break
                        else:
                            temp = f[temp]
        # print(f)                    
        hay_pos = 0
        need_pos = 0
        count = 0
        while hay_pos < len(haystack):
            # print(hay_pos,need_pos,count)
            if haystack[hay_pos] == needle[need_pos]:
                count += 1
                hay_pos += 1
                need_pos += 1
            elif count > 0 and haystack[hay_pos] != needle[need_pos]:
                need_pos = f[need_pos-1]+1
                count = need_pos
            elif need_pos == -1:
                need_pos = 0
                hay_pos += 1      
            else:
                hay_pos += 1
            
            if count == len(needle):
                return hay_pos - count
        return -1
        
        