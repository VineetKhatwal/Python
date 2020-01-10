class Solution:
    def isValid(self, s: str) -> bool:
        
        q = []
        
        if not s:
            return True
        
        l = len(s)
        
        if (l % 2 != 0):
            return False
        
        q.append(s[0])
        
        for i in range(1,l):
            if ((s[i]==')' and q[-1]=='(') or (s[i]==']' and q[-1]=='[') or (s[i]=='}' and q[-1]=='{')):
                
                q.pop()
                #print(q)
                
            else:
                q.append(s[i])
                #print(q)
                
        if q:
            return False
        else:
            return True
