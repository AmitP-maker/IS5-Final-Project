#PYTHOROID COUNT
# we begin with first number.
# Squaew the number and 2nd number and check with square of everyone except 1st and 2nd number
#Square the number and 3rd number and check with everyone except 1st and 3rd number.
#Square the number and 4th number and check with everyone except 1st and 4th.
#Run through the list.
#Sqaure of the 2nd and 3rd number and check with everyone except 2na and 3rd
my_list = [f for f in range(100)]


for n in range(len(my_list)):
    for k in range(n+1,len(my_list)):
        for j in range(len(my_list)):
            if (j == n or j == k): continue
            else: 
                if (my_list[n]**2 + my_list[k]**2 == my_list[j]**2):
                    print(my_list[n],my_list[k],my_list[j])

