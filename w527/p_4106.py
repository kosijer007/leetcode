class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        l = []
        temp = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if temp != []:
                    temp[0] = temp[0] + s1[i]
                    temp[1] = temp[1] + s2[i]
                else:
                    temp.append(s1[i]) 
                    temp.append(s2[i])
            else:
                if temp != []:
                    l.append(temp)
                temp =[]
        if temp != []:
            l.append(temp)
        return l
