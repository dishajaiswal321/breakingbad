# Input from user 
x=int(input("Enter the numbers in row wise: "))
y=int(input("Enter the numbers in coloumn wise: "))
matrix1=[]
print("Enetr the entries row wise: ")
for i in range(x):
    a=[]
    for j in range(y):
        a.append(int(input()))
    matrix1.append(a)
print("The first matrix is: ")
for i in range(x):
    for j in range(y):
        print(matrix1[i][j],end=" ")
    print()
#r=int(input("Enter the numbers in row wise: "))
#c=int(input("Enter the numbers in coloumn wise: "))
print("Enter the entries row wise: ")
matrix2=[]
for i in range(x):
    b=[]
    for j in range(y):
        b.append(int(input()))
    matrix2.append(b)
print("The second matrix is: ")
for i in range(x):
    for j in range(y):
        print(matrix2[i][j],end=" ")
    print()
matrix3=[]
for i in range(x):
    c=[]
    for j in range(y):
        c.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(c)
print("The addition of two matrices is: ")
for i in range(x):
    for j in range(y):
        print(matrix3[i][j],end =" ")
    print()

matrix4=[]
for i in range(x):
    d=[]
    for j in range(y):
        d.append(matrix1[i][j]-matrix2[i][j])
    matrix4.append(d)

print("The substraction of two matrices is: ")
for i in range(x):
    for j in range(y):
        print(matrix4[i][j],end =" ")
    print()
#multiplication of two matrix    
print("Multiplication of two matrix is: ")
c=[]
for i in range(x):
    h=[]
    for j in range(y):
        total=0 
        for k in range(y):
            total+=(matrix1[i][k]*matrix2[k][j])
        h.append(total)
    c.append(h)
for i in range(x):
    for j in range(y):
        print(c[i][j],end=" ")
    print()
#Transpose of matrix
print("Transpose of a first matrix is: ")
for i in range(x):
    for j in range(y):
        matrix1[i][j],matrix1[j][i]=matrix1[j][i],matrix1[i][j]
for i in range (x):
    for j in range(y):
        print(matrix1[i][j], end = " ")
    print()