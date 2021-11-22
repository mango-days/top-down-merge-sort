array=[10, 3, 19, 3, 7, 18, 4, 15, 5]

def re_arrange(array1, array2):
    ans=[]
    index1=0
    index2=0
    while (index1<len(array1) and index2<len(array2)):
        if array1[index1]>array2[index2]:
            ans.append(array2[index2])
            index2+=1
            if (index1==len(array1)):
                while(index2!=len(array2)): 
                    ans.append(array2[index2])
                    index2+=1
                break
        elif array1[index1]<array2[index2]:
            ans.append(array1[index1])
            index1+=1
            if (index2==len(array2)): 
                while(index1!=len(array1)): 
                    ans.append(array1[index1])
                    index1+=1
                break
        else:   # array1[index1]==array2[index2]:
            ans.append(array1[index1])
            ans.append(array2[index2])
            index1+=1
            index2+=1
            
        if (len(ans)==(len(array1)+len(array2))): break
    return(ans)
    
def separate(array):
    if (len(array)>1): 
        middle_index=int( len(array)/2 )
        ans1=separate(array[:middle_index])
        ans2=separate(array[middle_index:]
        ans=re_arrange (ans1 ,ans2)
        return (ans)
    return (array)
    
print(separate(array))
