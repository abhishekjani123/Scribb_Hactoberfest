day= int(input("Enter day: "))
a=0
if day>0 and day<=5:
  a = 0.40*day
if day>=6 and day<=10:
  a = 0.65*day
if day>10:
  a = 0.80*day
print("You have to pay",a,"rs as a fine")
