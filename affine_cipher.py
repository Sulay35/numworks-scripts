from math import *

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

def Eucle1(a,b):
  l1=[a,1,0]# a,u,v
  l2=[b,0,1]# b,u,v
  n=2
  while l1[0]%l2[0]!=0:
    r=l1[0]%l2[0]
    q=l1[0]//l2[0]
    l1,l2=l2,[r,l1[1]-q*l2[1],l1[2]-q*l2[2]] 
    n+=1
  return l2

def inv_mod(a,n):
  if Eucle1(a,n)[0]!=1:
    print("pgcd!=1")
  else:
    return Eucle1(a,n)[1]%n  

alpha="abcdefghijklmnopqrstuvwxyz"
def code(mot,a,b):
  f=lambda x:a*x+b
  mot_code=[]
  for l in mot:
    idx=alpha.index(l)
    val=f(idx)    
    r=val%26
    mot_code.append(alpha[r])    
  return mot_code

def decode(mot_code,a,b):
  mot=[]
  for l in mot_code:
    idx=alpha.index(l)
    inv=inv_mod(a,26)
    x=(inv*(idx-b))%26
    mot.append(alpha[x])
    
  return mot

def code_p(phrase,a,b):
  phrase_code=[]
  for mot in phrase:
    phrase_code.append(code(mot,a,b))
  return phrase_code

def decode_p(phrase_code,a,b):
  phrase=[]
  for mot in phrase_code:
    phrase.append(decode(mot,a,b))
  return phrase

p=split(input("phrase a code :"))
#p=split("maths abcd")
p_code=code_p(p,11,8)
print("p_code :", p_code)
p_decode=decode_p(p_code,11,8)
print("p_decode :", p_decode)
