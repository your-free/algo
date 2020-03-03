
def try_with_m(s, denom):
	
	flag =False
	m = max(denom)
	
	print(denom,s, m)
	denom.remove(m)
	c = 0
	while(s-m>0):
		s = s-m
		c+=1
	if(s-m==0):
		return c+1,True, denom
	else:
		denom2 = denom.copy()
		while(flag==False and len(denom2)>0):
			c2,flag,denom2 = try_with_m(s, denom2)
		if(flag):		
			c = c+c2
		return c, flag, denom

def solution(denom, total):
	if(total<=0):
		return 0;

	
	flag=False

	while(flag==False and len(denom)>0):

		count, flag, denom = try_with_m(total,denom.copy())
		print("not found--next iteration")

	if(flag):
		print('found a permutation')
		return count
	else:
		return -1

print(solution([186,419,83,408],6249))