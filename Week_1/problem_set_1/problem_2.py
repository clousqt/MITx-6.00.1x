# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#
# Number of times bob occurs is: 2
#

bob=0

for char in range(len(s)):
    if s[char:char+3]=="bob":
        bob+=1
    
print("Number of times bob occurs is: " + str(bob))
