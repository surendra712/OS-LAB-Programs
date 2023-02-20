n=int(input("Enter no of processes:"))
plist=[]
for i in range(n):
    pr=input("Enter name of process:")
    plist.append(pr)
print(plist)
bt=[]
for i in range(n):
    t=int(input("enter BT:"))
    bt.append(t)
print(bt)
at=[]
for i in range(n):
    a=int(input("enter arrival time:"))
    at.append(a)
ct=[]
k=at[0]+bt[0]
ct.append(k)
for i in range(1,n):
    if i==1:
        x=k+bt[i]
    else:
        x=x+bt[1]
    ct.append(x)
print("Completion time:",ct)
tat=[]
for i in range(n):
    tat.append(ct[i]-at[i])
print("TAT:",tat)
wt=[]                                                                     
for i in range(n):
    wt.append(tat[i]-bt[i])
print("WT:",wt)
s=0
for i in range(n):
    s=s+tat[i]
    avgtat=s/n
print("AVG TAT:",avgtat)
s1=0
for i in range(n):
    s1=s1+wt[i]
    avgwt=s1/n
print("AVG WT:",avgwt)