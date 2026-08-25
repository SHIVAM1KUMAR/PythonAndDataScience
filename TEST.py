#Printing Statement
print( 'Shivam kumar Starting...')
print(3,3.6,'shivam')

#Data Types
n=4#integer,n=3.5//float,
print(True)#Bool
print('Shivam')#String

#List/array
print([1,2])

#Tuples
print((1,2))

#set
print({1,2})

#Dictionary
print({'name':'Shivam','age':'22'})

#Type
type(3)

#Variable
n=8
print(n)

#Input
n=input("Enter value")
print(n)

#Type Conversion
x = 10  # Integer
y = 3.14  # Float

# Implicit conversion to float when performing division
z = x / y
print(z) 
x = 3.14
y = int(x)
print(y) 

#Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)