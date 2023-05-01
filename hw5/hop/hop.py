#!/usr/bin/env python
# coding: utf-8

# # HOP
# # Copyright: Jagadeesh Vasudevamurthy
# # filename: hop.ipynb

# In[16]:


import math
import random 


# # Solution.py
# # You write code in Solution.py

# In[17]:


############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################
############################################################
# All imports
###########################################################
from typing import List


class Solution:
  def __init__(self):
    ## YOU CANNOT ADD ANTHING HERE
    pass

  ##Required function to implement
  def hop_easy(self, A:List[int],f:'int') -> 'int':
    ## NOTHING CAN BE CHANGED HERE
    return self._hop_easy(A,f)

  ##Required function to implement
  def hop(self, A:List[int],f:'int') -> 'int':
    ## NOTHING CAN BE CHANGED HERE
    return self._hop(A,f)

  ########################################
  # TIME:THETA(N)
  # Space:THETA(1)
  # I have implemented the code. NOTHING CAN BE CHANGED HERE
  #########################################
  def _hop_easy(self, a:List[int],f:'int') -> 'int':
    ## n = len(a)  ##YOU CANNOT CALL len
    t = f
    h = 0
    while (True):
      if (a[t] == f):
        return h 
      else:
        t = a[t]
        h = h + 1
    return h

  ##Implement your code
  '''
   *  YOU CANNOT CHANGE INTERFACE OF THIS ROUTINE
	 *  YOU CANNOT USE ANY static variable in this function
	 *  YOU can use many local variables inside the function
	 *  Cannot use any loop statements like:  for, while, do, while, go to
	 *  Can use if
	 *  ONLY AFTER THE execution of this routine LIST a MUST have the same contents as you got it.
	 *  YOU cannot call any subroutine inside this function except _hop itself 
     *  DO NOT DO THIS
     *  a[:]
     * this is equivalent b = copy(a)
     * Note this makes deep copy. It is like calling a function in other languages
	 *  If your code is more than 10 lines, you don't understand the problem
	 '''
  ########################################
  # TIME:FILL
  # Space:FILL
  #########################################
  def _hop(self, a:List[int],f:'int') -> 'int':
    ## n = len(a)  ##YOU CANNOT CALL len
    if (a[f] == f):
      return 0
    #WRITE CODE
    #initialize a[f] and f to seperate variables.
    #this is done because we need to keep on swapping the 2 indices values until we find f at a[f] position
    i = a[f]
    j = f
    #now swap both the values at those indices
    a[i] , a[j] = a[j] , a[i]
    #now start the recusion function and assign it to a variable
    #count var keeps track of the number of hops
    #increment it by 1 at each hop
    count = self._hop(a,f) + 1
    #since the list 'a' values are not in original position, we need to re swap again
    a[i] , a[j] = a[j] , a[i]
    #finally return the count
    return count


# # util.py
# # Nothing can be changed

# In[18]:


############################################################
# Util.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
import sys # For getting Python Version
import random 
import math
from time import process_time 

class Util():
  pass

  ############################################
  # generate_random_number start to end INCLUDED 
  # start to end INCLUDED
  #########################################
  def generate_a_random_number(self,start:int,end:int)->'int':
    v = random.randrange(start,end+1);
    return v

  ############################################
  # generate_random_number GENERATES  N random numbers betweem 
  # start to end INCLUDED
  # if onlypositive is False, generates both pos and negative number
  #  randrange(beg, end, step) :- 
  #  beginning number (included in generation), 
  #  last number (excluded in generation) a
  #  nd step ( to skip numbers in range while selecting).
  #########################################
  def generate_random_number(self, N:int, onlypositive:bool, start:int, end:int)->'List of integer':
    a = []
    for i in range(N):
      v = self.generate_a_random_number(start,end);
      if (onlypositive == False):
        if ((i % 2) == 0): ##//Even. Half are positive, Half are negative
          v = -v ;
      a.append(v)
    return a

  ############################################
  # swap
  #########################################
  def swap(self,a:'List of integer', i:'int', j:'int'):
    t = a[i]
    a[i] = a[j]
    a[j] = t

  ############################################
  # generate shuffled number between 0 to n
  # n-1 not encluded
  #########################################
  def generate_suffled_number_between_1_to_n(self, n:int)->'List of integer':
    a = []
    for i in range(n):
      a.append(i)

    for i in range(n):
      j = self.generate_a_random_number(0,n-1);
      k = self.generate_a_random_number(0,n-1);
      self.swap(a,j,k)
    return a

  ############################################
  # generate shuffled number between 0 to n
  # n-1 not encluded
  #########################################
  def generate_duplicated_number_between_1_to_n(self, n:int)->'List of integer':
    a = []
    for i in range(n):
      a.append(i)

    for i in range(n):
      j = self.generate_a_random_number(0,n-1);
      k = self.generate_a_random_number(0,n-1);
      a[k] = a[j]
    return a

  ############################################
  # generate n numbers in ascending order from 0 to n-1
  #########################################
  def generate_n_numbers_in_ascending_order(self, n:int)->'List of integer':
    a = []
    for i in range(n):
      a.append(i)
    return a

  ############################################
  # generate n numbers in descending order from n-1 to 0
  #########################################
  def generate_n_numbers_in_descending_order(self, n:int)->'List of integer':
    a = []
    for i in range(n-1,-1,-1):
      a.append(i)
    return a

  ############################################
  # generate n same k number
  #########################################
  def generate_n_same_k_number(self, n:int,k:'int')->'List of integer':
    a = []
    for i in range(n):
      a.append(k)
    return a

  ############################################
  # print_index(10)
  #    0   1   2   3   4   5   6   7   8   9
  #########################################
  def print_index(self, n:int):
    for i in range(n):
      print("{:4d}".format(i),end="")
    print()

  ############################################
  # a = [7,8,9, 23, 100]
  # print_list(a)
  # 7   8   9  23 100
  #########################################
  def print_list(self, a:'list'):
    for i in range(len(a)):
      print("{:4d}".format(a[i]),end="")
    print()

  ############################################
  # a = [7,8,9, 1, 100]
  # crash
  #########################################
  def assert_ascending_range(self, a:'list',start:int, includingend:int):
    t = a[start]
    for i in range(start+1,includingend):
      if (a[i] < t):
        assert(False)
      t = a[i]

  ############################################
  # a = [7,8,9, 1, 100]
  # crash
  #########################################
  def assert_ascending(self, a:'list'):
    if (len(a)):
      self.assert_ascending_range(a,0,len(a)) 

  ############################################
  # a = [1,2,3, 3, 4]
  # return True
  #########################################
  def is_ascending_order_has_duplicates(self,a:'list')->'bool':
    if (len(a)):
        t = a[0]
        for i in range(1,len(a)):
          if (a[i] <= t):
            return True
          t = a[i]
    return False

  ############################################
  # log to the next possible integer
  #########################################
  def log_upper_bound(self, n:'int', b:'int')->'int':
    f = math.log(n,b)
    c = math.ceil(f)
    return c 

  ############################################
  # log to the smallest possible integer
  #########################################
  def log_lower_bound(self, n:'int', b:'int')->'int':
    f = math.log(n,b)
    c = math.floor(f)
    return c 

  ############################################
  # sqrt to the next possible integer
  #########################################
  def sqrt_upper_bound(self, n:'int')->'int':
    f = math.sqrt(n)
    c = math.ceil(f)
    return c 

  ############################################
  # sqrt to the smallest possible integer
  #########################################
  def sqrt_lower_bound(self, n:'int')->'int':
    f = math.sqrt(n)
    c = math.floor(f)
    return c 
   
  ############################################
  # TEST DRIVERS BELOW
  #########################################
  def _test_random(self,N:int, onlypositive:bool, start:int, end:int)->'None':
    a = self.generate_random_number(N,onlypositive,start,end);
    assert(len(a) == N)
    self.print_index(N)
    self.print_list(a)
    
  def _test_bed(self):
    self._test_random(10,True,30,100)
    self._test_random(10,False,30,40)
    
    n = 10
    a = self.generate_suffled_number_between_1_to_n(n)
    self.print_index(n)
    self.print_list(a)

    a = self.generate_n_numbers_in_descending_order(n)
    self.print_index(n)
    self.print_list(a)

    a = self.generate_n_numbers_in_ascending_order(n)
    self.print_index(n)
    self.print_list(a)

    a = self.generate_n_same_k_number(n,7)
    self.print_index(n)
    self.print_list(a)


# # HOP.py
# # Nothing can be changed in duplicateN.py

# In[19]:


############################################################
# Hop.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
#           NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
#from typing import List
#from Util import *
#from time import process_time 
#from Solution import *

class Hop():
  def __init__(self):
    self._show = False
    self._u = Util()
    self._testBench()

  def _hop_easy(self, a:List[int],f:'int') -> 'int':
    s = Solution()
    b = s.hop_easy(a,f)  # Function to implement
    return b

  def _hop(self, a:List[int],f:'int') -> 'int':
    s = Solution()
    b = s.hop(a,f)  # Function to implement
    return b
  
  #Private  function
  def _testBench(self):
    self._tests()
    self._testn()
    print("ALL TESTS PASSED")

     
  #Private sunction
  def _test1(self,a:List[int],f:'int'):
    b = a.copy()
    n = len(a)
    h1 = self._hop_easy(a,f)
    if (a != b):
      print("Array content changed after hop_easy")
      assert(False)
    h2 = self._hop(a,f)
    if (a != b):
      print("Array content changed after hop")
      assert(False)
    if (h1 != h2):
      print("Expected hop length =",h1, "But your length = ",h2)
      assert(False)
    if (self._show):
      n = len(a)
      print("-------Looking for",f,"------------------")
      self._u.print_index(n)
      self._u.print_list(a)     
      print("Num hopped:", h2)

  #Private sunction
  def _tests(self):
    self._show = True
    s = [5,1,0,4,2,3] 
    self._test1(s,3)

    for i in s:
      self._test1(s,i)


  #Private sunction
  def _testn(self):
    self._show = False
    n = 1000
    a = self._u.generate_suffled_number_between_1_to_n(n)
    print("----------",n,"tests------------")
    for i in a:
      self._test1(a,i)
    print("All",n, "Tests are passed. You are a genius")
      

############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing Hop.py Starts")
  s = Hop()
  print("Testing Hop.py Ends")
  print("Upload only Solution.py and output of the program as shown above")
  print("For A all tests must pass")

############################################################
# numCourses up
###########################################################
if (__name__  == '__main__'):
  main()
  
    



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




