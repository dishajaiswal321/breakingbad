n = int(input("Ente the number of students: "))
lst = []
for i in range(0, n):
    marks = int(input("Enter the maks of the student: "))
    lst.append(marks)
    print(lst)
absent = lst.count(-1)
summetion = sum(lst)+absent
avg = summetion / n
marks = set(lst)
marks1=marks.remove(0)
print("Number of students absent for the exam: ", absent)
print("Average marks of the student: ",avg)
print("Highest marks in the exam: ",max(marks))
print("Lowest marks in the exam: ",min(marks))
count = 0
temp =0 
index = 0
for i in range(0, len(lst)):
    temp = lst.count(lst[i])
    if(temp>count):
        count = temp 
        index =i 
most_frequent_number = lst[index]
print("The most frequent marks is: ",most_frequent_number)