'''Assgnment 3
@author: Ashish Patel
'''
#1

words=input("enter string:")
output=[]
word=''
for i in words:
    if i == ' ':
        output.append(word)
        word=''
    else:
        word+=i
if word:
    output.append(word)
print(output)

#2

words=input("enter string:")
output=[]
word=''
for i in words:
    if i == ' ':
        output.append(word)
        word=''
    else:
        word+=i
if word:
    output.append(word)
for j in range(len(output)):
    swapped = False
    i = 0
    while i<len(output)-1:
        if output[i]>output[i+1]:
            output[i],output[i+1] = output[i+1],output[i]
            swapped = True
        i+=1
    if swapped == False:
        break
print (output)