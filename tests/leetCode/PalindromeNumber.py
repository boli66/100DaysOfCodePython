class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = ""
        x = str(x)

        for i in range(len(x)-1,-1,-1):
            s+=x[i]

        if(s == x):
            return True
        else:
            return False