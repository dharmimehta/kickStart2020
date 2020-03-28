def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
    ss=0
    count=0
    for i in range(n+1): 
        flag=0
        for w in range(W+1):
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
                if flag==0:
                    ss=ss+val[i-1]
                    count=count+1
                    flag=1
            else: 
                K[i][w] = K[i-1][w] 
    return ss, count
  
stack= int(input(""))
W=int(input(""))
tempW=W
W=W-1
val=[]
for i in range(0,stack):
    temp = input("")
    temp = list(temp.split(" "))
    temp = list(map(int,temp))
    val.append(temp)

val1 = [10,10,100,30] 
val2 = [80, 50,10,50]
wt = [1, 2, 3, 4] 
n = len(val1)-1 

for i in range(1,stack):
    for j in range(1,stack):
        if val[i][0]>val[j][0]:
            val[i],val[j]=val[j],val[i]

finalLast=0
countSum=0

for i in range(0,stack):
    if(countSum>=tempW):
        break
    final,c = knapSack(W, wt, val[i], n)
    countSum = countSum+c
    W=W-c+1
    finalLast = finalLast+final

print(finalLast)
