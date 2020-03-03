inf = 1e3
graph_matrix = []

def inform_network(node,k):
	
	n = len(graph_matrix[0])
	change_list = []
	for i in range(0,n):
		if(i!=k):
			if(graph_matrix[node][i] != inf):
				w = graph_matrix[k][node] + graph_matrix[node][i]
				print(w,graph_matrix[k][i])
				if(graph_matrix[k][i] > w):
					graph_matrix[k][i] = w
					print("changed")
					change_list.append(i)
				if(node==k and i not in change_list):
						change_list.append(i)

	for change in change_list:
		inform_network(change, k)



def delay(times, n, k):
	# n = number of nodes
	# k = start node in the graph
	not_reached = set()
	reached = set()
	k = k - 1
	
	for i in range(n):
		graph_matrix.append([inf]*n)
		graph_matrix[i][i] = 0
		not_reached.add(i)
	
	for time in times:
		a1,a2,t1 = time[0]-1, time[1]-1, time[2]
		graph_matrix[a1][a2] = t1
	
	# based on our representation in the graph
	print("before network delay")
	for row in graph_matrix:
		print(row)

	inform_network(k, k)
	
	print("----afterwrds -----")
	for row in graph_matrix:
		print(row)

	for i in range(0,n):
		if(i!=k):
			if(graph_matrix[k][i]==inf):
				return -1

	return max(graph_matrix[k])		
print("network delay is :",delay([[1,2,1]],2,1))

#print("network delay is :",delay([[2,1,5],[2,3,8],[1,3,2],[3,4,10]], 4,2))

'''
print(delay([[4,2,76],[1,3,79],[3,1,81],[4,3,30],
[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],
[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],
[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],
5,
3))

'''