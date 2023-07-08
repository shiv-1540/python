import numpy as np
a=np.loadtxt('testmarks1.csv',delimiter=',',skiprows=1,dtype=float)
print("Testmarks1 is :")
print(a)

b=np.loadtxt('testmarks2.csv',delimiter=',',skiprows=1,dtype=float)
print("Testmarks2 is:")
print(b)

#1 Arithematic operation
#1 Addition of testmarks
print("\n Addition of Testmarks1 & Testmarks2 is :")
print(np.add(a,b))

#2 Substraction of a & b
print("Substraction of Testmarks1 & Testmarks2 is:")
print(np.subtract(a,b))

#3 Multiplication of a & b
print("\n Multiplication of testmarks1 & testmarks2 is:")
print(np.multiply(a,b))

#4 Transpose of matrices
print("\n Transpose of matrix testmarks1 is:")
print(np.transpose(a))
print("\n Transpose of matrix testmarks2 is:")
print(np.transpose(b))

#5 Inverse of matrix


#2 stastical operations
#1 Mean of matrices
print("Mean of matrix a is:")
print(np.mean(a,0))

print("Mean of matrix b is :")
print(np.mean(b,0))

#2 Max of columns in a
print("Max of columns in a is:")
c=np.max(a,0)
print(c)

#3 standard Deviation
sd=np.std(a[0])
print("Standard deviation is:")
print(sd)




#Horizontal & Vertical stacking of arrays
result=np.hstack((a,b))
print("The horizontal stacking of the datasets is:")
print(result)

result=np.vstack((a,b))
print("The vertical stacking of the datasets is:")
print(result)

#Custom Sequence generation
seq_gen=[]
for i in range(len(a)):
    seq_gen.append(a[i])
    seq_gen.append(b[i])
print(seq_gen)

# Bitwise Operators
#Bitwise and
print("a[0][2]",a[0][2])
print("a[0][3]",a[0][3])

bitwise_and=np.bitwise_and(int(a[0][3]), int(a[0][2]))
print("Bitwise and of ",a[0][2],"&",a[0][3],"is:")
print(bitwise_and)

#Bitwise or
bitwise_or=np.bitwise_or(int(a[0][3]),int(a[0][2]))
print("Bitwise or: ",bitwise_or)


#Copying & Viewying of arrays
cparr=np.copy(a[0])
a[0,0]=172

print("a[0] is:",a[0])
print("copy of array is:",cparr)

viwarr=b[0].view()
b[0,0]=182

print("b[0]",b[0])
print("view array ",viwarr)

a1=np.arange(1,10)
b1=np.arange(10,100,10)
print('matrix a1 is :\n',a1)
print('matrix b1 is :\n',b1)

c=a1.reshape(3,3)
d=b1.reshape(3,3)
print('matrix a1 after reshape :\n',c)
print('matrix b1 after reshape :\n',d)


#Bitwise operator
#bitwise
print('two elemets of a1 and b1 -',a1[0],b1[0])
print('bitwise and of two elements: \n',np.bitwise_and(a1[0],b1[0]))
print('bitwise or of two elements: \n',np.bitwise_or(a1[0],b1[0]))
print('bitwise not of  element: \n',a1[0],'-',np.invert(a1[0]))
print('left shift of  element: \n',a1[0],'-',np.left_shift(a1[0],3))
print('right shift of  element: \n',a1[0],'-',np.right_shift(a1[0],4))


#Mathematical Operations
#1 Square root
sqrt=np.sqrt(a)
print("Square root of testmarks1 elements is:")
print(sqrt)

#2 Exponential
exp=np.exp(a)
print("Exponential od testmarks1 elements is:")
print(exp)

print('Original array:\n',a)
print('After rounding:\n',np.around(a))

print('The original array:\n' ,b)
print('The floor function array:\n', np.floor(b))
print('The ceil function array:\n',np.ceil(b))


#Stacking along axis=-1
stacked = np.stack((a,b),axis=-1)
print("Stacking along axis=-1 i.e.last dimension is:")
print(stacked)

#Broadcasting
print("Testmarks1 804 ")
print("Before Broadcasting:")
print(a[3])
mul_arr=a[3]*3
print("After broadcasting:")
print(mul_arr)

#sorting,searching and counting

print('Sort along column:\n',np.sort(a, axis = 0))

print(' searching of Indices of elements > 100 \n',np.where(a > 100))

print('counting elements greater than 800',np.count_nonzero( a>800))

#broadcasting
a1=np.array([1,2,3,4,5])
c1=np.add(a,a1)
print('matrix a \n',a,'\n a1 \n',a1)
print('addition of a and a1 with broadcasting a1 :\n',c1)











