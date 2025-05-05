 #Sequence Sum 
n=int(input('Enter Number'))
fact=1
result=0
for i in range(1,n+1):
    fact=fact*i
    result=result +i/fact

    print(result)


#Nested loop
for i in range(1,5):
    for j in range(1,5):
        print(i,j)

        #PATTERNS


rows=int(input('Enter rows value')) 
for i in range(1,rows+1): 
    for j in range(1,i+1):   
        print('*',end='')
        print()  


R=int(input('Enter R value'))
for i in range(1,R+1):
    for j in range(1,i):
        print(j,end='')
        for k in range(i-1,0,-1):
            print(k,end='')
        print()  


        #Break
for i in range(1,10):
    if  i == 5:
     break
print(i)

#Continue
for i in range(1,10):
    if  i == 5:
     continue
print(i)


#Pass
for i in range(1,10):
    pass





