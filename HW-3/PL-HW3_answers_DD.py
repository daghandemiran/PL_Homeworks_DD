# coding=utf-8
# -*- CODİNG:8 -*-

# HW-3 answers for Alfa Programming Language Course Lecture-4

# Program name: PL-HW3_answers_DD.py
# Written by: Daghan Demiran
# Date: 31-03-2016
# Version : 1.0

print "____________________________"  # nothing but separator

print '''Problem #1 Write a Python code that takes a string from user and  reverse the first half of a string,  then
append it to the end of second half of  the string.Print latest version  of the string.

Input: Any string from user '''

# Solution 1

word = raw_input("Enter a string: ")
w_lenght = len(word)
rev_word = word[0:w_lenght / 2]
answer = word[w_lenght / 2::1] + rev_word[::-1]

print "#1 Answer is : ", answer


print "____________________________"  # nothing but separator


print '''Problem #2 Write a Python code that takes a string from user and checks whether the string is palindrome
(reads the same backward or forward). E.g. 'radar', 'racecar'

Input: Any string from use '''

# Solution 2

word = raw_input("Enter a string: ")
rev_word = word[::-1]
if word == rev_word:
    print "#2 Answer is : It is palindrome"
else:
    print "#2 Answer is : It is not palindrome"


print "____________________________"  # nothing but separator


print '''Problem #3 Write a Python code that take 2 strings from user.First string contains mixed characters
(e.g. ‘*a+,b-1/2c’). Second string contains only alphabetical letters.For alphabetical characters in first string,
find number of occurrence in second string.

Input:
1.input: string
2.input: string '''

# Solution 3
K_1 = raw_input("Enter a string you want to find: ")
K_2 = raw_input("Enter a string you want to search: ")

for i in K_1:
    print "#3 Answer is : " + i,"--->", K_2.count(i)


print "____________________________"  # nothing but separator
