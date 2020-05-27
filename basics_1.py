# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:55:20 2020

@author: rouss
"""


print('Hello World!')

age,name=20,"Zach"

print(age)
print(name)

age1=12
age2=18

x="yee"
y=10*x
print(y)


#PLACEHOLDERS
sentence= "The quick brown fox jumps over the lazy dog"
print(sentence[0:3]) 
#Don't need 0 if starting at 0 for splice

sent="%s is 20 years old"
print(sent%name)

sent2="%s %s is the President of the United States"
print(sent2%("Donald", "Trump"))

sent3="%s is %d years old"
print(sent3%("Jacob", 19))


##MAKING LISTS
list1=["Apples", "oranges", "Bananas","Cheese"]
print(list1[:3])
list1.append("blueberries")
print(list1)
list1[0]="cherries"
print(list1)
del list1[2]
print(list1)
list2=["a","b","c"]
print(list1+list2)

list3=[2,4,8,28,3,-1]
print(max(list3),min(list3))

family=["Kristen",49,"Jacob",19,"Thomas", 54, "TJ", 24]

familydic={"Kristen":49,"Jacob":19,"Thomas":54,"TJ":24}
print(familydic)
print(familydic["Kristen"])
familydic["Jacob"]=20
del familydic["TJ"]
print(familydic)
print(len(familydic))
#Each key must be unique

#Tuples
tup =("oranges","apples","bananas")
tup2=(12,13)
tup3=tup+tup2
print(tup3)

##If/ELSE loops
if 0==0:
    print('something')
else: 
    print('nothin')
    ##use shift+tab to line up else
   
age=15
if(age>=13 and age < 18):
    print('You are a teen')
else:
    print('You are not a teen')

## FOR loops    
for item in list1:
    print(item)
    
tup3=(13,12,15)
for items in tup3:
    print(items)
    
for i in range(0,10):
    print(i)
    
for i in range(0,11,2):
    print(i)
    #2 is increment factor
for i in range (0,100,20):
    print(i)
    
for x in range (0,300,30):
    for y in range (0,10,1):
        print(x*y)
 
c=0       
while c<5:
    print(c)
    if c==3:
        break
    c=c+1
#break ends a loop   
#continue skips remining code and codes back to top of loop
  
##Functions
def Helloworld():
    print('Hello World')
    
Helloworld()

def Greeting(name):
    print("Hi "+name+'!')
    
Greeting(name)

def Add(var1,var2):
    print(var1+var2)
    
Add(10,3)

def returnAdd(var4,var5):
    return(var4+var5)

sum=returnAdd(10,3)
print(sum)