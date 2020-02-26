#moving_avg.py

inl = [10,20,30,10]

avg = 0
for idx in range(0,len(inl)):
	s = avg*idx + inl[idx]
	avg = s/(idx+1)
	print(avg)
