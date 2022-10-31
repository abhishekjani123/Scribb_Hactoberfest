num =[None]*3 
odd_num = []
for i in range(0,3):
  num[i]=int(input("num %d:"%(i+1)))
count = 0 
for i in range(0,3):
  if(num[i]%2!=0):
    odd_num.append(num[i])
    count = count +1
print("Odd Numbers:",odd_num)
print("Total Odd Numbers : %d"%(count))
print("Maximum odd number is :",max(odd_num))
