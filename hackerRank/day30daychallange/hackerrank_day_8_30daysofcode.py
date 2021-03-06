# -*- coding: utf-8 -*-
"""Hackerrank day 8 / 30daysOfCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ObhYmKdvJJpwV11pYEK3ln1pyZIYR24F
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Read the input and assemble the phone book
n = int(input())
phonebook = {}
for i in range(n):
    contact = input().split()
    phonebook[contact[0]] = contact[1]


# processing the queries

lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phonebook:
        print(name + "=" + str(phonebook[name]) )
    else:
        print("Not found")