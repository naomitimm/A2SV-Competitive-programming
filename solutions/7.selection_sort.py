def selectionSort(arr):

    for i in range(len(arr)):
        currentMin = arr[i]
        for index in range(len(arr)):
            if(arr[index] > currentMin):
                arr[i] , arr[index] = arr[index] , arr[i]
                currentMin = arr[index]
    print(arr)
 

selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])