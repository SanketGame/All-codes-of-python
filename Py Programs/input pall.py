L=[]

I1=input("E1:")
L.append(I1)
I2=input("E2")
L.append(I2)
I3=input("E3")
L.append(I3)

L1=L.copy()
print("\n",L1)
L1.reverse()

print("\n",L1==L)

if(L1==L):
    print(L," \nis a Palledrome:)\n")
else:
    print(L,"\n IS Not a Palledrome:(\n")

