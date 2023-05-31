def selection_sort(arr):
    for i in range(len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr

arr=[21,45,36,19,40,83,9,34,12]
print(selection_sort(arr))
