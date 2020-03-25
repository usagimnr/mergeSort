########################################
#                                
# This program will perform merge sort which is a recursive algorithm. 
# It will continually divide the inputted list in half until it is 
# successfully sorted. Once sorted the lists will be merged meaning it
# will be combined back into a sorted new list.   
#
########################################

def merge(list1, list2):
    #Creates a new list to input the merging of both seperate lists given
    newList = []
    i = 0
    j = 0
    #Append the lower value number for the lists into the new and removes that from
    #it's original list to compare is with the next number until one of the list
    #don't have anymore values left
    while len(list1) != 0 and len(list2) != 0:
        if list1[i] < list2[j]:
            newList.append(list1[i])
            list1.remove(list1[i])
        elif list1[i] > list2[j]:
            newList.append(list2[j])
            list2.remove(list2[j])

    #If a list had any left over values it will add it to the end of the new list
    if len(list1) == 0:
        newList += list2
    else:
        newList += list1

    return newList

def mergeSort(numList):
    #Will return the original list if it has one or no values, otherwise it will
    #split the left in half, seperate it from it's left and right side and recursively
    #keep doing that until it is sorted
    if len(numList) == 0 or len(numList) == 1:
        return numList
    else:
        midpoint = int(len(numList)/2)
        left = mergeSort(numList[:midpoint])
        right = mergeSort(numList[midpoint:])
        return merge(left,right)