def cns(n):
    #create an empty dictionary to store the number and its count as key, value pair.
    num_count = {}
    #create an empty string that stores the final result.
    res_str=""

    #iterate over the given string.
    for i in n:

        #if number is not in dictionary -> add the number and assign value of 1 to it.
        if i not in num_count:
            num_count[i]=1
        
        #if number already exists in dictionary -> increment it's value by 1.
        else:
            num_count[i]+=1

    #finally, iterate over this dictionary to store the result in a string as required
    for i, j in num_count.items():
        res_str+=str(j)+i
    
    #return the result string
    return res_str


n = '9876543210'
print(cns(n))

#OR -> OTHER WAY TO SOLVE
'''
#create 2 variables, that can be used as string index and increments over time 
    #starting from 1st and 2nd element of the string
    l=0
    r=1
    #let count be 1 since minimum count of a number is 1
    count=1
    #create an empty string to store the result
    res=""
    
    #iterate over the while loop until 'r' is greater than the length of n. 
    while(r<=len(n)):
        
        #if r is lesser than the length of n and element of n in position l is equal to r's position ->
        #increment count by 1
        #increment l and r by 1
        #reason - > if both elements are same, count is increased. Then l and r are moved by 1 step
        if r <=len(n) - 1 and n[l]==n[r]:
            count+=1
            l+=1
            r+=1
        
        #else -> now oth are elements are different. So concatenate count and value in l position to res
        #then, move l and r by 1 step. 
        #reset count value to 1
        #reason -> since both the elements are now different, we need to add the count of previous element to result string
        else:
            res+=str(count)+n[l]
            l+=1
            r+=1
            count = 1
    
    #return the result string
    return res
'''