#Print First 10 natural numbers using while loop

'''
x = {"brand" : "volkswagen",
     "model":"polo",
     "year" : "2020",
     "color" : "black",
     "engine" : "1800cc"}

print("the brand of car is : ",x["brand"])
print("the model of car is : ",x['model'])
print("the year of car is :",x['year'])
print('the color of car is : ',x['color'])
print('the engine is: ',x['engine'])

x['color']= 'white'  #update
x['transmission']='automatic'  #insert new keys and value
x.pop('color') # for delete the key and value
del x['year']
x['color']= 'white'
x['year']= '2020'

print(x)


for i in x:
    print(i,x[i])
    

#for i in x.keys():
if "polo" in x.keys():     #it is mandatory to add values to print values otherwise it will print keys
    print("yes")
else:
    print("no")
    #print(i)

print(x.keys())
print(x.values())
#print(x.item())

cars = {"car1":{'model':'polo','brand':'german','engine':'1200cc'},
        'car2':{'model':'i30','brand':'british','engine':'1800cc'},
        'car3':{'model':'i20','brand':'irish','engine':'1900cc'}}
print(cars["car3"]["engine"])

y = cars.items()
print(y)
'''

# Write a Python script to sort (ascending and descending) a dictionary by value.



x = {'a':1,'d':4,'e':5,'b':2,'c':3}
a = dict(sorted(x.items()))
print(a)
b = dict(sorted(x.items(),reverse=True))
print(b)


#Write a Python script to add a key to a dictionary.

x = {'a':1,'d':4,'e':5,'b':2,'c':3}
x['f']=6
print(x)

#Write a Python script to concatenate following dictionaries to create a new one.

i = {1:10, 2:20}
j = {3:30, 4:40}
k = {5:50,6:60}
b = {}
for x in (i,j,k):b.update(x)
print(b)

#Write a Python script to check whether a given key already exists in a dictionary
z = {'a':1,'d':4,'e':5,'b':2,'c':3}

def exist_key(x):
     if x in z:
          print("the key is already existed ")
     else:
          print("not existed")

#h = input('enter the key: ')
#exist_key(h)

# Write a Python program to iterate over dictionaries using for loops.

w = {'a':1,'d':4,'e':5,'b':2,'c':3}

for i in w.items():
     print(i)
for i,j in w.items():
     print(i,"is equal to",j)

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 1:1*1
a = dict()
for i in range(1,6):
     a[i]=i*i
print(a)

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

e = dict()
for i in range(1,16):
     e[i]=i*i
print(e)

#Write a Python script to merge two Python dictionaries

a = {'a':2,'b':3,"c":4}
b = {'d':5,"e":6,'f':7}
c = {}
for i in (a,b):c.update(i)
print(c)

#Write a Python program to sum all the items in a dictionary.

a = {'a':2,'b':3,"c":4}
b = sum(a.values())
print(b)

#Write a Python program to multiply all the items in a dictionary.

a = {'a':2,'b':3,"c":4}
c = 1
for i in a:
     c = c*a[i]
print(c)


#Write a Python program to remove a key from a dictionary

w = {'a':2,'b':3,"c":4}
del w['a']
w['e'] = 56
print(w)

#Write a Python program to map two lists into a dictionary

i = ['red', 'green', 'blue']
j = ['#FF0000','#008000', '#0000FF']

z = dict(zip(i,j))
print(z)


student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}
x = {}
for i,j in student_data.items():
     if j not in x.values():
          x[i]=j

print(x)



print(student_data)

a = {'s':{'d':86,'r':898},'e':{"g":9794},'w':{'a':4646,'m':1213,'n':9994}}
print(a.keys())
print(a.values())
print(a.items())


#18. Write a Python program to check a dictionary is empty or not

#Write a Python program to combine two dictionary adding values for common keys
from collections import counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = counter(d1)+counter(d2)
print(d)

#'c:\program files (x86)\python38-32\python.exe -m pip install --upgrade pip' command.