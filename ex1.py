#To display the biggest odd integer in the list...
lst=[]
odd=[]
print("Enter 10 integers: ")
for i in range(0,10):
    value= int(input())
    lst.append(value)
    if (value%2)!=0:
        odd.append(value)
length=len(odd)
if length!=0:
    big=odd[0]
    for j in range(1,length):
        if big<odd[j]:
            big=odd[j]
    print("The biggest odd number is the list is: ", big)
else:
    print("No odd number in the list.")
        
        
    



