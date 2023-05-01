def cns(n):

    #return "1" if n is 1. this is the base case required for recursion
    if n == 1:
        return "1"

    else:
        #begin recursion and assign the result of each recursive function to a variable - recurs
        recurs = cns(n-1)
        #create an empty string to store the result
        res = ""
        #begin the count of elements with 1
        count = 1

        #iterate over the length of recurs variable (it changes at each recursion)
        for i in range(len(recurs)):
            #check if i is not in the last position and if i and i+1 index of recurs is equal
            if i!=len(recurs)-1 and recurs[i]==recurs[i+1]:
                #increment count by 1. since both elements and same
                count+=1

            #if i and i+1 index of recurs are not same
            else:
                #concatenate count and ith value of recurs to res
                res+=str(count) + recurs[i]
                #reset count as it should begin from first from next elements. (as both elements are different)
                count = 1

        return res

print(cns(5))