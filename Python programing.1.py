import time

print("Enter first number: ",end="")
f_num = eval(input())
print("Enter second number ",end="")
s_num = eval(input())

print("-------------------------------------")
print("Your Entries: ")
print("First number: ",f_num)
print("Second number: ",s_num)

"""
if f_num > s_num:
    print("Greater number: ",f_num)

if s_num > f_num:
    print("Greater number: ",s_num)

"""

if f_num > s_num:
    print("True, Greater number: ",f_num)
else:
    print("False, Greater number: ",s_num)


time.sleep(2.4)
#input()
