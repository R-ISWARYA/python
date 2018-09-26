N=int(input("NUMBER="))
if(N<=1000):
flag=0
for x in range(1,N+1):
if(N%x==0):
flag=flag+1
if(flag==2):
print("PRIME")
else:
print("NOT A PRIME")
else:
print("the input size is invalid")
