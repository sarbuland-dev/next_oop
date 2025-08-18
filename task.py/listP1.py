x=[2,3,4,59,6,7,8,4,5,6]
y=[]
target=61
for i in range(len(x)):
    for j in range(i+1,len(x)) :
        if x[i]+x[j]==target:
            
            
            
            y.append((x[i],x[j]))
        
print(y)

        