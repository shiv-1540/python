import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.arange(10,100,10).reshape(3,3)

print("The array x is :")
print(x)
print("The array y is:")
print(y)

z=np.add(x,y)
print("The element wise addition of martrix is:")
print(z)

z=np.subtract(x,y)
print("The subtarction of two matrix is:")
print(z)

z=np.multiply(x,y)
print("The multiplication of two matrix is:")
print(z)

z=np.divide(x,y)
print("The division of two matrix is:")
print(z)

z=np.invert(x)
print("The inverse of x is :")
print(z)

z=np.transpose(x)
print("The transpose of x is:")
print(z)

z=np.amax(x)
print(z)

