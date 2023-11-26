#COUNTANDSAY
#if there is single  value and n = 1, then print it

#if n is more than 1, repeat for n times.

#Start with 2nd variable and see if it same as 1st variable.
#    If yes, then 
#        pop first variable
#        increment the count
#        check 1st - 2nd variable variable# because first variable is gone.
 #   If no, then
 #       insert count as 1st variable.
 #       initialize count as 1
 #       jump to 3rd variable for checking.
  
def countsay(n_list,n):     
    i = 1
    count = 1
    if (n == 1):
        return n_list
    else:
        n_list.insert(0,str(count))
        print(n_list)
    while (i < n):
        j = 0
        count = 1
        while j < len(n_list):
            if (len(n_list) == j+1):
                n_list.insert(j,str(count))
                #print(n_list)
                break
            if (n_list[j] == n_list[j+1]):
                #print(n_list[j], n_list[j+1])
                count = count + 1
                n_list.pop(j)
            else:
                n_list.insert(j,str(count))
                count = 1
                j = j + 2
            #print(j, len(n_list), count, n_list)
        i = i + 1
        print(n_list)
    return n_list
    
p = countsay(['1'], 10)
