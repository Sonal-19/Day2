"""Square pattern program"""
# for i in range(0, 5):                         # Create a list of rows
#     for j in range(0, 5):                     # Create a list of columns
#         print("*", end="")
#     print()

"""Program to print half pyramid using"""
# for x in range(1, 5):
#     for y in range(1, x+1):
#         print("*", end = " ")
#     print()

# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print()

"""Program to print half pyramid a using numbers"""
# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()

"""Program to print half pyramid using alphabets"""
# rows = int(input("Enter number of rows: "))
# ascii_value = 65
# for i in range(rows):
#     for j in range(i+1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")
#     ascii_value += 1
#     print()

"""Inverted half pyramid using"""   
# for x in range(5):
#     for y in range(5-x):
#         print("*", end = " ")
#     print()

# rows = int(input("Enter number of rows: "))
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
#     print("\n")

"""Inverted half pyramid using numbers"""
# rows = int(input("Enter number of rows: "))
# for i in range(rows, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

"""Program to print full pyramid using"""
# for x in range(1, 5):
#     for y in range(1, x+1):
#         print("*", end = " ")
#     print()
# for x in range(5):
#     for y in range(5-x):
#         print("*", end = " ")
#     print()

"""Program to print full pyramid using"""
# rows = int(input("Enter number of rows: "))
# k = 0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
#     k = 0
#     print() 

"""Full Pyramid of Numbers"""
# rows = int(input("Enter number of rows: "))
# k = 0
# count=0
# count1=0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print("  ", end="")
#         count+=1
#     while k!=((2*i)-1):
#         if count<=rows-1:
#             print(i+k, end=" ")
#             count+=1
#         else:
#             count1+=1
#             print(i+k-(2*count1), end=" ")
#         k += 1
#     count1 = count = k = 0
#     print()
#     rows = int(input("Enter number of rows: "))

"""Inverted full pyramid of"""
# for i in range(rows, 1, -1):
#     for space in range(0, rows-i):
#         print("  ", end="")
#     for j in range(i, 2*i-1):
#         print("* ", end="")
#     for j in range(1, i-1):
#         print("* ", end="")
#     print()

