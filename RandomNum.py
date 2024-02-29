import random

#print(random.randint(1,80))

#print(random.random())

#Program to print yes, no, maybe when a dice is rolled

answer= random.randint(1,3)
if answer==1:
  print("Yes")
if answer==2:
  print("No")
if answer==3:
   print("Maybe")