

# print("hello")

#  2 . Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# n = int(input());
# if n%2==0:
#     print("Not Weird")
# else:
#     print("Weird")

# actual solution

# n = int(input());
# if n%2==1:
#     print("Weird")
# elif n%2 ==0 and 2<= n <=5:
#     print("Not Weird")
# elif n%2 ==0 and 6<= n <=20:
#     print("Weird")
# elif n%2 == 0 and n>20:
#     print("Not Weird")
# else:
#     print("wrong input")


# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# a = int(input())   
# b = int(input())
# print(a+b)
# print(a-b)
# print(a*b)


# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# approch 1

# a = int(input())
# b = int(input())
# c = int(a/b )   # typecasting
# print (c)
# d= a/b
# print (d)

# approch 2 

# a = int(input())
# b = int(input())
# c = a/b   
# print (int(c))# typecasting
# d= a/b
# print (d)


# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# method - 1

# n = int(input())
# x=1
# while x <= n:
#     print (x,end='')
#     x += 1

# method 2

# print(*range(1, n+1),sep='')



def is_leap(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))







