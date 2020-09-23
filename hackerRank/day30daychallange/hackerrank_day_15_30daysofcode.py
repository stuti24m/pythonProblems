# -*- coding: utf-8 -*-
"""Hackerrank_day_15_30daysofcode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AFRwl0Ta19eFhuiZt3QVX0MGFYHjpLwm
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
      temp = Node(data)  
      if head is None:
        head = temp
        return head
      current = head
      while current.next is not None:
        current = current.next

      current.next = temp
      return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);