# a = 15
# b = 4
# if (a>b):
#     print("hello")

"""a = 15
b = 140
if (a > b):
    print("hello")
else:
    print("hi")"""

# b = 40
# c = 45
# if(b>c):
#     print('h')
# else:
#     print('l')


"""a = 14
b = 20
c = 64
if(b>c):
    print('h')
elif(a>c):
    print('l')
elif(b==c):
    print('r')
else:
    print('s')"""

# for x in range(10):
#     print(x)

# for x in range(21,31):
#     print(x)

# conditional statements
# if statement 
a= 4
b= 3
if (a>b):
    print ("hello")


# if else statement 
a= 4
b= 7
if (a>b):
    print ("hello")
else:
     print ("h")

a= 14
b=20
c=64
if (b>c):
   print ("H")
elif (a>c):
    print ("L")
elif (b==c):
    print ("R")
else:
    print ("LH")


# looping statements
for x in range (10):
    print(x)


for x in range (10):
     for y in range (11,15):
       print (x,y)


row = int(input("Enter number of rows: "))
print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()


# while loop
a=10
while (a<=100):
    print ("hello")  


# break    
num = 0
for i in range(10):
	num += 1
	if num == 8:
		break
	print("The num has value:", num)
print("Out of loop")

num = 0
for i in range(10):
	num += 1
	if num == 5:
		break
	print("The num has value:", num)
print("Out of loop")


# continue
# Python program to
# demonstrate continue
# statement

for i in range(1, 11):
	if i == 6:
		continue
	else:
		print(i, end=" ")