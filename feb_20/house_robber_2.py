

idx_dict= {}
flag1 = False
flag2 = False

def solution(hl): 
	# hl = house list
	n = len(hl)
	for idx in range(0,len(hl)):
		idx_dict[idx] = (-1, [])
	idx_list = []	
	max_sum , idx_list = dp(hl[0:n-1],0)
	
	return max_sum

def dp(hl, idx):
	n = len(hl)
	#print("len:" , n)
	max_sum = -1
	il = None
	
	if(idx > n -1):
		return 0,[]

	if(idx_dict[idx][0]!=-1):
		return idx_dict[idx][0],idx_dict[idx][1]

	if(idx == n-1):
		print(" last element ", hl[idx])
		il = []
		il.append(idx)
		max_sum = hl[idx]
	else:
		#print(dp(hl, idx+2))
		sum1 , il1  = dp(hl, idx+2) 
		sum2 , il2  = dp(hl, idx+1)
		sum1 += hl[idx]
		#print("sum1:",sum1)
		#print("sum2:",sum2)
		if(sum1>sum2):
			il1.append(idx)
			max_sum = sum1
			il = il1
		else:
			il = il2
			max_sum = sum2

		if(idx==0):
			print("before circular removal:",il)	
			b = n-1
			c = 0
			
			if(0 in il or b in il):
				if(0 in il):
					c+=hl[0]
				if(b in il):
					
					c+=hl[b]
				print( sum1-c, sum2+hl[n-1])
				if((sum1-c )< (sum2 + hl[n-1])):
					print("making change as the last element greater")
					max_sum = max_sum - c + hl[n-1]	+ sum2
			else:
				print("adding last element as the first and second last not there")
				max_sum+=hl[n-1]


	idx_dict[idx] = (max_sum, il)
	return max_sum, il 

hl = [0,2,0,4]
print(solution(hl))

