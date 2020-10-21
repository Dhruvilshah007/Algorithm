import sys 
A = [68, 25, 19, 22, 13,28] 
  
# Traverse through all array elements 
for i in range(len(A)): 
      
  
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  
