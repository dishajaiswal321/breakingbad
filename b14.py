arr = []
n = int(input("Enter Number of Students:" )) 
for i in range(n):
    ele = float(input("Enter marks of the student %d: " %(i+1)))
    arr.append(ele)   
#Function for selection sort
def selection_sort(arr, n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(arr[j]<arr[i]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            ++j
        ++i
selection_sort(arr, n)
print("Using Selection Sort")
print("The sorted list in ascending order is: ",arr)

#Function for bubble sort
def bubble_sort(arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        ++j
    ++i
bubble_sort(arr, n)
print("Using Bubble Sort")
print("The sorted list in ascending order is: ",arr)
#Displaying top 5 marks from the list
print("Top Five Scores are...")
for i in range(0, 5):
    print(arr[n - i - 1])
