#!usr/bin/python
@author:Ashish Patel
'''Homework'''

#1)write python program in following way
'''
print('''my name is "Ashish". I love coding''')
print('''This is 'my first program'.''')

x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))
print("Value1=",x,end=",")
print("Value2=",y,end=",")
print("Value3=",z)
'''

#2

print("Hello! my name is Ashish")
print("Hello I am a candidate")
print("234.56")
print("34")
print("a+3j")

#3
x=10+20*(45+67.0)
complex(x)
print(type(x))

#4
data = int(input("Please Enter your number:"))
if data%2==0 and data%5==0:
	print("Hurray it is what i a looking for")
else:
	print("wrong input")

#5
x=int(input("Enter number:"))
if x in range(10,51):
    print("yes i am in range")
else:
    print("Oops")

#Assignment 2

#1)
'''while i am solving this i got subscrible error sir can you help me to understand this'''
x[4][2]
x[4][6]
x[4][4][2:4]
x[4][3:5]

#2

#6
x=input("Enter words:")
words=x.split()
for i in words:
    print("The length of",x,"is:",len(i))
