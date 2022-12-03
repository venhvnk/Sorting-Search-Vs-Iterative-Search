

import time
import random as rn
import numpy as np
import matplotlib.pyplot as plt



#sorting selection
def selectionSort(T):
    for i in range(len(T)-1):
        min = i
        for j in range(i+1,len(T)):
            if T[j]<T[min]:
                min = j
        s = T[i]
        T[i] = T[min]
        T[min] = s





#linear search algo
def rechercheSequentielle(T,val):
    i = 0
    while i<len(T)-1 and val != T[i]:
        i+=1

    if T[i] == val:
        print("found x")
    else:
        print("x was not found")

#iterative search

def rechercheDichotomiqueIterative(T,val):

    first = 0
    last = len(T)-1

    while first<=last:
        m = (first+last)//2
        if T[m] == val:
            return "found x"
        elif T[m]<val:
            first = m+1
        else:
            last = m-1
    return "x was not found"

#recursive search

def rechercheDichotomiqueRecursive(T,val,first,last):
    if first>=last:
        return "x was not found"
    else:
        m = (first+last)//2
        if T[m] == val:
            return "found x"
        elif T[m] < val:
            return rechercheDichotomiqueRecursive(T, val, m+1, last)
        else:
            return rechercheDichotomiqueRecursive(T, val, first, m-1)


#here we send an array and display it
def afficheTab(T):
    for tt in T:
        print(tt)




#main



#Size of Arrays 
x =[1000,1200,1980,2000,6030,5000,7930]

#used time to find the element
y1 =[] #rechercheSequentielle
y2 =[] #rechercheDichotomiqueIterative
y3 =[] # rechercheDichotomiqueRecursive

Tab = [] #the array where we are going to search

for i in range(len(x)): #loop manipulates through size array

    Tab = np.random.randint(1, 10001, x[i]) #put random numbers between 1 and 10001 and the size of it changes from size array

    val = rn.randint(1,10001) #wanted number takes a random value
    print(i) #display that im in the index i in th array

    selectionSort(Tab)#function to sort the array

    start = time.perf_counter()#variable that holds current time in search algorihtm
    rechercheSequentielle(Tab, val)#call the function to search for the number in the array
    end = time.perf_counter()#variable holds time after the search
    y1.append(end-start)#calculate search time

    #same thing for other methods
    start = time.perf_counter()
    print(rechercheDichotomiqueIterative(Tab, val))
    end = time.perf_counter()
    y2.append(end-start)

    start = time.perf_counter()
    print(rechercheDichotomiqueRecursive(Tab, val, 0, len(Tab) - 1))
    end = time.perf_counter()
    y3.append(end-start)

#here we're going to draw the graph
plt.figure(num=0,dpi=120)#create a graph with its value and image size
plt.plot(x,y1,label="rechercheSequentielle")#to draw sequentielle graph
plt.plot(x,y2,label="rechercheDichotomiqueIterative")
plt.plot(x,y3,label="rechercheDichotomiqueRecursive")
plt.xlabel("Taille")
plt.ylabel("Temps")
plt.legend() #to display graph labels
plt.show()#to show the graph