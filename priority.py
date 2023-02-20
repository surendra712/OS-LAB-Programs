n=int(input("Enter no of processes:"))
print("Enter pid bursttime priority:")
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
         if l[i][2]>l[j][2]:
             l[i],l[j]=l[j],l[i]
ct=0
for i in range(n):
    ct+=l[i][1]
    l[i].append(ct)
print("pid BT Priority AT TAT WT")
tat,wt=0,0
for i in range(n):
    print(l[i][0]," ",l[i][1]," ",l[i][2]," ",0," ",l[i][3]," ",l[i][3]-l[i][1])
    tat+=l[i][3]
    wt+=l[i][3]-l[i][1]
print("AVGTAT:",tat/n)
print("AVGWT:",wt/n)