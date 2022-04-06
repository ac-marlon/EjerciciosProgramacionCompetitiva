# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:00:49 2022

@author: Marlon
"""

# Easy problems for HackerEarth

"""

PROBLEM:

You are required to enter a word that consists of X and Y that denote the 
number of Zs and Os respectively. The input word is considered similar to 
word zoo if 2 * X = Y.

Determine if the entered word is similar to word zoo.

"""

# Zoos (own solution)

word = input()

if word.count('z') * 2 == word.count('o'):
    print("Yes")
else:
    print("No")
    
"""

PROBLEM:

You are provided an array A of size N that contains non-negative integers. 
Your task is to determine whether the number that is formed by selecting 
the last digit of all the N numbers is divisible by 10.

"""

# Divisibility (own solution)

N = int(input())
A = int(''.join([i[-1] for i in input().split()]))

if A % 10 == 0:
    print("Yes")
else:
    print("No")

"""

PROBLEM:

You live in a village. The village can be represented as a line that contains  
grids. Each grid can be denoted as a house that is marked as H or a blank 
space that is marked as "." (a dot).

A person lives in each house. A person can move to a grid if it is adjacent 
to that person. Therefore, the grid must be present on the left and right 
side of that person.

Now, you are required to put some fences that can be marked as B on some blank
spaces so that the village can be divided into several pieces. 
A person cannot walk past a fence but can walk through a house. 

"""

# Split houses (own solution)

import re

n = int(input())
village = input()

if len(re.findall('H{2,}', village)) != 0:
    print("NO")   
elif (village[0] == 'H') or (village[-1] == 'H'):
    new_village = village.replace('.', 'B')
    print("YES")
    print(new_village)
elif len(re.findall('H\.\.H', village)) != 0:
    new_village = village.replace('.', 'B')
    print("YES")
    print(new_village)
else:
    fences = len(min(re.findall('\.+', village)))
    print("YES")
    new_village = village.replace('.', 'B')
    print(new_village.replace('B' * fences + 'H' + 'B' * fences,
                              '.' * fences + 'H' + '.' * fences))
    
"""

PROBLEM:

You are given an array A of size N that contains integers. Here, N is an even 
number. You are required to perform the following operations:
    
- Divide the array of numbers in two equal halves.
Note: Here, two equal parts of a test case are created by dividing the array 
into two equal parts.
- Take the first digit of the numbers that are available in the first half of 
the array (first 50% of the test case).
- Take the last digit of the numbers that are available in the second half of 
the array (second 50% of the test case).
Generate a number by using the digits that have been selected in the above 
steps.

Your task is to determine whether the newly-generated number is divisible by 11.

"""

# Divisible (own solution)

N = int(input())
A = input().split()
digit = int(''.join(i[0] for i in A[:N//2]) + ''.join(i[-1] for i in A[N//2:]))

if digit % 11 == 0:
    print("OUI")
else:
    print("NON")
