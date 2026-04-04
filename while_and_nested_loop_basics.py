#while loop 
i=1
while i<=10:
 if i% 6 == 0:
   break
 print(i)
 i +=1

#break+continue 
i=1
while i<=30:
   if i == 28:
       break
   if i% 4 == 0:
      i +=1
      continue
   if i% 3 == 0 and i% 5 == 0:
      print("threefive")
   elif i% 3 == 0 :
      print("three")
   elif i% 5 == 0:
      print("five")
   else:
      print(i)
  i +=1

#nested loop
for i in range(1, 4):
  j = 1
  while j <= i:
     print(j, end=' ')
     j += 1
  print()

# rectangle pattern

rows=int(input('enter number of rows'))
columns=int(input('enter number of coulmns'))
symbol=(input('type of symbol'))

for i in range(rows):
   for j in range(columns):
      print(symbol,end=(""))
   print()

#reverse triangle 

num=1
for i in range (5,0,-1):
  j=1
  while j<=i:
    if num% 3 ==0:
       num+=1
       continue
    if num% 5 == 0:
       print("five",end=" ")
    else:
       print(num,end=" ")
    num+=1
    j+=1
  print()

# each row 5 number

count = 0

for num in range(1, 31):
    
    if num == 25:
        break

    if num % 4 == 0:
        continue

    print(num, end=" ")
    count += 1

    if count == 5:
        print()
        count = 0

#skip + continue + triangle

  rows = 6
num = 1

for i in range(1, rows+1):
    j = 1
    while j <= i:
        if num % 2 == 0:
            num += 1
            continue

        if num % 3 == 0 and num % 5 == 0:
            print("threefive", end=" ")
        elif num % 3 == 0:
            print("three", end=" ")
        elif num % 5 == 0:
            print("five", end=" ")
        else:
            print(num, end=" ")

        num += 1
        j += 1
    print()
