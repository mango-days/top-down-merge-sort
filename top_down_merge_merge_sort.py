array=[10, 3, 19, 3, 7, 18, 4, 15, 5]

def sort(array1, array2):
    ans=[]
    index1=0
    index2=0
    while (index1<len(array1) and index2<len(array2)):
        if array1[index1]>array2[index2]:
            ans.append(array2[index2])
            index2+=1
        elif array1[index1]<array2[index2]:
            ans.append(array1[index1])
            index1+=1
        else:   # array1[index1]==array2[index2]:
            ans.append(array1[index1])
            ans.append(array2[index2])
            index1+=1
            index2+=1
            
        if (index1==len(array1)):
            while(index2!=len(array2)): 
                ans.append(array2[index2])
                index2+=1
        elif (index2==len(array2)): 
            while(index1!=len(array1)): 
                ans.append(array1[index1])
                index1+=1
                
        if (len(ans)==(len(array1)+len(array2))): break
    return(ans)
    
def separate(array):
    right_index=len(array)
    left_index=1
    if (len(array)>1): 
        bisection=int(left_index + (right_index-1)/2)
        ans=(sort (separate(array[:bisection]),separate(array[bisection:])))
        return (ans)
    return (array)
    
print(separate(array))