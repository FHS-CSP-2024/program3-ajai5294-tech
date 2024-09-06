## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is "+name+","" I am",age,"years old")
print()
print("my skills are")
print(" -", skill1,"("+level1+")")
print(" -", skill2,"("+level2+")")
print(" -", skill3,"("+level3+")")
print()
print("I am looking for a job with a salary of " +str(lower)+"-" +str(upper)+" dollars per month")


print("\n")


## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")
print("X val: " +x)
print("Y val: " +y)
print()
sum = int(x)+int(y)
diff = int(x)-int(y)
mult = int(x)*int(y)
div = int(x)/int(y)
print(x+ " + "+y+" = " + str(sum))
print(x+ " - "+y+" = " + str(diff))
print(x+ " * "+y+" = " + str(mult))
print(x+ " / "+y+" = " + str(div))

