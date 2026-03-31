# grading
y=int(input('enter number'))

if y>= 90 :
    print("A")
elif y>= 75 :
    print("B")
elif y>= 50 :
    print('c')
elif y>= 0 :
    print('fail')
else:
    print('ivalid')

#lncreasing and decreasing
x=int(input('enter number'))
y=int(input('enter number'))
z=int(input('enter number'))
  
if x == y == z :
    print('all equal')
elif x == y or y==z or x==z:
    print('two equals')
elif x< y< z :
    print("increasing")
elif x> y> z :
   print('decreasing')
else:
    print("neither")

#middle number
x=int(input('enter number'))
y=int(input('enter number'))
z=int(input('enter number'))


if x == y or y == z or z == x :
    print('no unique middle')
elif (x<y and x>z) or (x>y and x<z):
     print(" x is in middle")
elif (y<x and y>z)or (y>x and y<z) :
    print('y is a middle')
else:
    print(' z is in middle')

#largest and smallest number
a=int(input('enter number'))
b=int(input('enter number'))
c=int(input('enter number'))

 # equality checks
if a== b== c :
    print('all are equal')
elif a== b :
    print('a andb are equal')
elif b== c :
    print('b and c are equal')
elif c== a:
    print("c and a  are equal")
# largest number 
if a> b and a > c:
    print('a is largest')
elif b> a and b> c :
    print('b is largest')
else :
    print('c is largest')
# smallest number
if a< b and a< c:
    print( 'a is smallest')
elif b< a and b< c:
    print('b is smallest')
else:
    print(' c is smallest')

# loops 
#for loops
# odd and even
for i in range (1,16):
  if i% 2== 0:
     print(i,"even")
  else:
     print(i,"odd")

  # fizz buzz
  for i in range(1 , 31):
    if i% 3 ==0 and i% 5 == 0 :
        print("fizzbuzz")
    elif i% 3 ==0:
       print('fizz')
    elif i% 5 == 0:
       print('buzz')
    else :
       print(i)

# loop + condition
for i in range (1,21):
   if i% 5 == 0 :
      print(i,"five")
   elif i% 3 == 0:
        continue
   else:
      print(i)

     
    
