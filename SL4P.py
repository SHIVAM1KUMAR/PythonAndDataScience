s=input('enter String')
#print(len(s))
counter=0
for i in s:
   counter=counter+1

print(counter)#find length of string

#Extraxt user name before @
s=input('enter Email')
pos=s.index('@')
print(s[0:pos])

#Frequency find 
s=input('enter String')
term=input('What u want to search')
counter=0
for i in s:
   if i==term:
      counter +=1

print('Frequency',counter)

#remove a word
s=input('enter String')
term=input('What u want to remove')
for i in s:
   if i !=term:
      result=result+i

print(result)     


#Palindrome
s=input('enter String')
flag=True
for i in range(0,len(s)//2):
   if s[i] !=s[len(s)-i-1]:
      flag=false
      print('not palindrome')

if flag:
   print('Palindrome')

 #split
"hi how are u".split()
s=input('enter String')
L=[]
temp=''
for i in s:
   if i !='':
      
     temp=temp+i
   else:
      L.append(temp)

print(L)  

#Title
"Hi my name is sjivam".title()
s=input('enter String')
L=[]
for i in s:
   L.append(i[0].upper()+i[1:].lower())

print(L)
