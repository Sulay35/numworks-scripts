from math import *

# Function made to split an arry into separated array 
# according to the separator chosen, by default it's a blank space

def split(array,sep=" "):
  i=0
  splited=[]
  while i<len(array):
    word=[]
    for j in range(i,len(array)):
      l=str(array[j])
      if l==" ":
        i+=1
        break
      else:
        word.append(l)
      i+=1
    splited.append(word)  
  return splited
