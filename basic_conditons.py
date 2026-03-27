#Even and Odd 
number=7
 
if number %2 == 0:
  print("even")
else:
  print("odd")

#positive and negative
x=4
if x> 0 :
   print('positive')
elif x< 0:
   print('negative')   
else:
   print('zero')   

#fizzbuzz
y=9
if y% 3 == 0 :
   print('frizz')
elif y% 5 == 0:
   print('Buzz')
elif y% 3 == 0 and y% 5 == 0 :
   print('FizzBuzz')
else:
   print('y')
