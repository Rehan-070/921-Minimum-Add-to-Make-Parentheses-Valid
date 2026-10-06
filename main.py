class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # o=s.count('(')
        # c=s.count(')')
        # return max(o,c)-min(o,c)

        o=0
        a=0

        for i in s:
            if i == '(':
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    a+=1
        return a+o
