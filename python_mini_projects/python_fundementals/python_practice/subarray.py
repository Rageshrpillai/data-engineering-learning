arr = [0, 2, -3, 3, -1, 2, -2]


# loop through main array 
# declare total =0 cuz every time we need to reset the array to zero after finding a sum of zero array
# define a for loop again for checking for running total
# check if the total is zero if so store it  in maxarray  then check max array with existing maxarray to 
# which  one is max using max function


def  longest_subarray(arr):
    max_array=-1
    start_index=-1
    end_index=-1

    for i in range(len(arr)):
        total_sum=0
        for j in range(i,len(arr)):
            total_sum+=arr[j]
            if total_sum == 0:
                sums=j-i+1
                max_array =max(sums,max_array)
                start_index=i
                end_index=j
                
    

    return max_array , start_index , end_index


print(longest_subarray(arr))

        