x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=int(input("enter the third number:")) 
if(x>y):
  if(x>z):
    print(x,"is big")
  else:
    print(z,"is big")
else:
  if(y>z):
    print(y,"is big")
  else:
    print(z,"is big")
