

idx_dict= {}

def solution(hl): 
	# hl = house list
	
	for idx in range(0,len(hl)):
		idx_dict[idx] = -1

	max_sum = dp(hl,0)b
	return max_sum

def dp(hl, idx):
	n = len(hl)
	max_sum = -1
	if(idx > n -1):
		return 0
	if(idx_dict[idx]!=-1):
		return idx_dict[idx]

	if(idx == n-1):
		#print("last elemt in the list:",hl[idx])
		max_sum = hl[idx]

	else:
		sum1 = dp(hl,idx+2)+hl[idx]
		sum2 = dp(hl, idx+1)
		#print("sum1:",sum1)
		#print("sum2:",sum2)
		if(sum1>sum2):
			max_sum = sum1
		else:
			max_sum = sum2

	idx_dict[idx] = max_sum
	return max_sum 

hl = [2,7,9,3,1]
print(solution(hl))