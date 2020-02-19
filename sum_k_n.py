## hackerearth coding problem

## max sum for X, going from 1 - N


n = 3 #input()
print("input N:",n%2)

max_sum = 0

for k in range(1,n+1):
    sum = 0
    for i in range(1,k+1):
        sum+= pow(-1,i+1)*i*(i+1)
    print("k", k," sum:", sum)
    if(sum>max_sum):
        max_sum=sum

print(max_sum)
