import re
from typing import List
from collections import Counter
from enum import Enum
from functools import reduce


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

class Solution5:
    @staticmethod
    def count_unique_words(s: str) ->int:
        words = s.split()
        cnt = Counter(words)
        unique_count = len(words)
        for w in words:
            if cnt[w] > 1:
               unique_count -= 1
        return  unique_count       

class Solution6:
    @staticmethod
    def count_avg_word_length(s: str) ->int:
        words = s.split()
        avg_cnt = 0
        total_length = 0
        for w in words:
            total_length += len(w)
            avg_cnt = total_length / len(words)
        return round(avg_cnt)
class Solution7:
    @staticmethod
    def count_avg_word_length_set(s: set) ->int:  
        total_length = sum(len(e) for e in s)  
        return round(total_length/len(s))
    
class Solution8:
    @staticmethod
    def count_substr_instr(s: str, subs: str) ->int:  
        parts = s.split(subs)  
        return len(parts) -1    
class Solution9:
    @staticmethod
    def is_palindrome(n: int) ->bool:  
        s = str(n)
        j = len(s) - 1
        f = True
        for i in range(len(s)):
            if i > j:
                break
            if s[i] != s[j]:
                f = False
                break
            j -= 1
        return f  

class Solution10:
    @staticmethod
    def balance_ints(n: [int]) ->dict:  
        cnt = Counter(n)
        mx = max(cnt[c] for c in cnt)
        bal = {}
        for c in cnt:
            if cnt[c] < mx:
                bal[c] = mx - cnt[c]
        return bal   
    
class Solution11:
    @staticmethod
    def count_str_n_format(s: str) ->str:  
        r = ""
        check = {}
        for i in range(len(s)):
            if s[i] not in check:
                r += s[i] + str(s.count(s[i])) 
                check[s[i]] = s[i]

        return r  

class Solution12:
    @staticmethod
    def is_valid_ip(s: str) ->bool:  
        parts = s.split(".")
        if len(parts) != 4:
            return False
        
        for p in parts:
            if int(p) < 0 or int(p) > 255:
                return False 
        

        return True         


class Solution13:
    @staticmethod
    def replace_none_with_last_notnone(ar: [any]) ->[any]:  
       
        last_non_none = None
        for i in range(len(ar)):
            if ar[i] is not None:
                last_non_none = ar[i]
            else:
                ar[i] = last_non_none

        return ar            
        

        return True         

class Solution14:
    @staticmethod
    def find_mismatch_btw_2_lists(ar1: [str], ar2: [str]) ->[str]: 
        ret = []
        ar = ar1 + ar2

        cnt = Counter(ar)

        for i in cnt:
            if cnt[i] == 1:
                ret.append(i)

        return ret
    
class Solution15:
    @staticmethod
    def n_largest_dict_val(d: dict, n: int) ->dict:     
        sorted_vals = [d[k] for k in d]
        sorted_vals.sort()
        return {n:sorted_vals[n-1]}

class Solution16:
    class types(Enum):
        UP = 1
        DOWN = 2
        FLAT = 3
    @staticmethod
    def is_monothonic(a: [int]) ->bool: 
        if len(a) < 2:
            return True
        # find type
        mon = True
        if a[0] == a[1]:
            t = Solution16.types.FLAT

        if a[0] > a[1]:
            t = Solution16.types.DOWN

        if a[0] < a[1]:
            t = Solution16.types.UP

        for i in range(len(a)):

            if i < len(a) - 1:
                if t == Solution16.types.FLAT:
                    if a[i] != a[i+1]:
                        mon = False
                        break
                elif t == Solution16.types.UP:    
        
                    if a[i] > a[i+1]:
                        mon = False
                        break
                elif t == Solution16.types.DOWN:    
        
                    if a[i] < a[i+1]:
                        mon = False
                        break    

        return mon

class Solution17:
    @staticmethod
    def map_reduce_filter_comprehension():

        lst = [1,2,3,4,45,16]

        flt_lst = list(filter(lambda x: x > 4, lst))

        map_lst = list(map(lambda x: x * 2, lst))

        com_lst = ["< 3" if x < 3 else "> 3" for x in lst]

    @staticmethod
    def sums_of_nums():

        # Input: nums = [1,2,3,4]
        # Output: [1,3,6,10]
        # Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]   
        nums = [1,2,3,4] 
        nnums = []
        n = 0
        for num in nums:
            if n == 0:
                nnums.append(num)
            else:        
                nnums.append(reduce(lambda x, y: x + y, nums[0:n+1]))
            n += 1    

        strs = ["hello1", "hello2", "hello3", "hello4", "hello5", "hello5"]
        z = zip(strs[0:4], nums[0:4])
        ns = nums.append(strs)
        sets = set(strs)

    def remove_k_elems():
        # Input: arr = [4,3,1,1,3,3,2], k = 3
        # Output: 2
        # Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.    
        arr = [4,3,1,1,3,3,2]
        arrc = Counter(arr)

        return

       
    
def main():
    #print(Solution2.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]) )
    #print(Solution.reverseOnlyLetters("r2st-gTp!"))  
    #print(Solution3.minAddToMakeValid(s="((())))))"))
    #print(Solution4.minFlipsMonoIncr(s = "0011000"))
    #print(Solution5.count_unique_words("this is just is a start b start c"))
    #print(Solution6.count_avg_word_length("1 22 33 4444 55555"))
    #print(Solution7.count_avg_word_length_set({"1", "22", "33", "4444", "55555"}))
    #print(Solution8.count_substr_instr("aastringaa", "aa"))
    #print(Solution8.count_substr_instr("aastring", "aa"))
    #print(Solution8.count_substr_instr("stringaaprin", "aa"))
    #print(Solution9.is_palindrome(12344321))
    #print(Solution9.is_palindrome(1234321))
    #print(Solution9.is_palindrome(12347321))
    #print(Solution10.balance_ints([1,1,2]))
    #print(Solution10.balance_ints([1, 1, 1, 5, 3, 2, 2]))
    #print(Solution11.count_str_n_format("I am back."))  
    #print(Solution12.is_valid_ip("174.233.0.1"))
    #print(Solution12.is_valid_ip("17a.276.0.1"))
    #print(Solution12.is_valid_ip("174.233.-1.0"))
    #print(Solution13.replace_none_with_last_notnone([1,2,3,None, None,4,5]))
    #print(Solution13.replace_none_with_last_notnone([None,8, None]))
    #print(Solution14.find_mismatch_btw_2_lists(["this", "is", "my", "test"], ["this", "is", "my", "array"]))
    #print(Solution15.n_largest_dict_val({"a": 1, "b": 2, "c": 100, "d": 30}, 2))
    # print(Solution16.is_monothonic([ 1, 2, 5, 5, 8]))
    # print(Solution16.is_monothonic([ 9, 6, 6, 4, 3]))
    # print(Solution16.is_monothonic([ 1, 1, 1, 1]))
    # print(Solution16.is_monothonic([ 9, 6, 6, 4, 10]))
    Solution17.remove_k_elems()
    #Solution17.map_reduce_filter_comprehension()
    #Solution17.sums_of_nums()

if __name__ == "__main__":
    main()
