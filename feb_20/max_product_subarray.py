def solution(nums):
	arr = nums
	dp_dict=[]
	n = len(arr)
	
	for i in range(0, n):
		dp_dict.append([])

		dp_dict[i] = [0]*(n-i)

	if(n==0):
		return 0
	
	if(n==1):
		return arr[0]

	step_size=0

	maxpro = -1e7 
	for ss in range(0,n):
		for i in range(0,len(arr)-ss):
			p = arr[i]
			
			for j in range(i+1,ss+i+1):
				
				p = p*arr[j]
				
			
			dp_dict[ss][i] = p		
			if(p>maxpro):
				maxpro = p
	print(dp_dict)
	return maxpro

print(solution([2,3,-2,4,1]))




