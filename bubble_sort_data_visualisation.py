from math import *
from random import *
from kandinsky import *
from random import *
from time import *
from ion import *
L=330
l=222

elt_nb=int(input("number of elements"))
d=[i for i in range(elt_nb)]
#c=[color(random()*255,random()*255,random()*255) for i in range(101)]
#c=[color(255,183,52) for i in range(elt_nb)]
c=[color((i*255)/elt_nb,(i*183)/elt_nb,(i*52)/elt_nb) for i in range(elt_nb)]

def mix(lst):
  n=[]
  nc=[]  
  for i in range(len(lst)):
    rdm=choice(lst)  
    idx=lst.index(rdm)
    #fill_rect(int(idx*(L/101)),l,3,int(-(222*(222/100))),"white")#fill_rect(int(idx*(L/101)),l,3,int(-(222*(222/100))),"white")    
    n.append(rdm)
    #fill_rect(int((n.index(rdm)+1)*(L/101)),l,3,int(-(rdm*(222/100))),"red")       
    lst.remove(rdm)
  return n

def draw(lst):
  fill_rect(0,0,L,l,"white")
  for i in range(len(lst)):
    col=c[i]
    v=d[i]
    fill_rect(int(i*(L/len(lst))),l,3,int(-(v*(222/(len(lst)-1)))),col)
    sleep(0.01)  

comp=0
def bubble(lst):
  for i in range(len(lst)-1):
    #comp+=1
    if lst[i+1]<lst[i]:
      fill_rect(int(i*(L/len(lst))),l,3,int(-(lst[i]*(222/(len(lst)-1)))),"white")
      fill_rect(int((i+1)*(L/(len(lst)))),l,3,int(-(lst[i+1]*(222/(len(lst)-1)))),"white")
      
      tmp=lst[i]
      lst[i]=lst[i+1]
      lst[i+1]=tmp
      
      t=c[i]
      c[i]=c[i+1]
      c[i+1]=t

      fill_rect(int(i*(L/(len(lst)))),l,3,int(-(lst[i]*(222/(len(lst)-1)))),c[i])
      fill_rect(int((i+1)*(L/len(lst))),l,3,int(-(lst[i+1]*(222/(len(lst)-1)))),c[i+1])
      sleep(0.001)      

def process(lst):
  while d!=[i for i in range(len(lst))]:  
    bubble(d)

while 1:
  draw(d)
  d=mix(d)
  c=[c[i]for i in d]
    
  
  draw(d)
  process(d)
  draw_string(str(comp),int(330/2),int(222/2))  
  #comp=0
  sleep(5)
