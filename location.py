x = [23,45,675,33,76,98,90,45]
# loc=0
for i in range (len(x)):
    if x[i]==76:
     print(i)
     
print("-------------")
     
for i in x:
    # if x[i]==76:
     print(i)
     
print("-------------")     
     
for index, value in enumerate(x):
    if value == 76:
        print(index)
print("------using while loop-------") 
      
i=0
while i<(len(x)):
    # print(x[i])
    if x[i]==90:
        print(f"location of 90 is {i}")
        break
    i+=1