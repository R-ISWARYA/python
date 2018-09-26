s=int(input("s="))
e=int(input("e="))
if(s<=100000)&(e<=100000):
for x in range(s+1,e):
if(x%2!=0):
print(x)
else:
print("input is invalid")
