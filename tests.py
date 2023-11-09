import re
from typing import List
from collections import Counter

class Solution:
    @staticmethod
    def reverseOnlyLetters(s: str) -> str:
        j = len(s) - 1
        i = 0
        b = []
        b.extend(s)
        for x in range(len(s)):
            #re.match(r'[A-Za-z]', string[index])
            if s[i].isalpha() == True:
                if s[j].isalpha() == True:
                    tmp = b[j]
                    b[j] = b[i] 
                    b[i] = tmp
                    j -= 1
                    i += 1
                else:
                    j -= 1        
            else:
                i += 1    
            if i == j:
                break        
        s = ""       
        return s.join(b)


class Solution2:
    @staticmethod
    def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
        r = []
        for w1 in words1:
            i = 0
            for w2 in words2:
                if w1.find(w2) >= 0:
                    i += 1
                else:
                    break
            if i == len(words2):
                r.append(w1) 

        return r        

class Solution3:
    @staticmethod
    def minAddToMakeValid(s: str) -> int:
        c = Counter(s) 
        
        n = abs( c.get('(', 0) - c.get(')',0) )
        return n


class Solution4:
    @staticmethod
    def minFlipsMonoIncr(s: str) -> int:
        f = 0
        
        for i in range(len(s)-1):
            if s[i] == '0':
                if s[i+1] == '1':
                    f +=1

            else:
                if    s[i+1] == '0':
                    f +=1

        return f       

def main():
    #print(Solution2.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]) )
    #print(Solution.reverseOnlyLetters("r2st-gTp!"))  
    print(Solution3.minAddToMakeValid(s="((())))))"))
    print(Solution4.minFlipsMonoIncr(s = "0011000"))
      

if __name__ == "__main__":
    main()
