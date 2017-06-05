#   Assume s is a string of lower case characters.
#
#   Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
#   Longest substring in alphabetical order is: beggh
#
#   In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
#   Longest substring in alphabetical order is: abc


streak = ''
answer = ''
for char in s:
    #Assign streak the first character of s if streak is empty
    if streak == '':
        streak = char
        
    #If the character is <= the last in streak, add to the end of streak
    #reminder: 'a'>'b' returns False
        
    elif streak[-1] <= char:
        streak += char
        
    #If the last character in streak is greater than the last...
    elif streak[-1] > char:
        
        #Check if the current streak is the longest, if so assign its value to answer
        if len(streak) > len(answer):
            answer=streak
            
        #Assign streak the current char
        streak = char
        
#Final check just in case answer is empty. Give it the current streak
if len(streak) > len(answer):
    answer=streak  
    
print("Longest substring in alphabetical order is: " + str(answer))   
