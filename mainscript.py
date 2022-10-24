#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:10:02 2022

@author: nicholasojo
"""

def partition(array, low, high):
 
   
    pivot = array[high]
 
   
    i = low - 1
 
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
   
    return i + 1
 

 
 
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        
        quickSort(array, low, pi - 1)
 
       
        quickSort(array, pi + 1, high)
 
 
data = [449, 48, 242, 44, 65, 520, 332, 173, 931, 667, 146, 640, 448, 522, 820, 
964, 688, 840, 113, 325, 950, 754, 999, 723, 909, 956, 255, 972, 111, 543, 
282, 443, 362, 968, 725, 549, 356, 828, 566, 193, 107, 982, 580, 606, 882, 
834, 236, 655, 604, 731, 321, 465, 814, 441, 460, 277, 29, 476, 126, 382, 
101, 27, 135, 944, 307, 220, 51, 153, 536, 711, 901, 507, 139, 94, 155, 
214, 724, 315, 33, 267, 782, 816, 75, 489, 835, 224, 532, 996, 573, 479, 
729, 484, 505, 508, 875, 709, 589, 425, 454, 702]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)