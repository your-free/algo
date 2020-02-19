

def search_pattern(char_list,idx, i,j, board):
	if(idx >=len(char_list)):
		print("word found:")
		return True
	#print(i,j)	
	oldc = board[i][j]
	board[i][j]= '*'
	found = False
	nextc = char_list[idx]
	
	
	if(i-1>=0):
		up = board[i-1][j]
		if(up==nextc):
			#print(up,i-1,j)
			found = search_pattern(char_list,idx+1, i-1,j, board)
			if(found):
				print("up found")
				return found

	
	if(j+1<n):
		right = board[i][j+1]		
		if(right==nextc):
			#print(right,i,j+1)
			found = search_pattern(char_list,idx+1, i,j+1, board)
			if(found):
				print("right found")
				return found
	if(i+1<m):

		down = board[i+1][j]		
		#print("down:",down, nextc)
		if(down==nextc):
			#print(down,i+1,j)
			found = search_pattern(char_list,idx+1, i+1,j, board)
			if(found):
				print("down found")
				return found

	if(j-1>=0):
		left = board[i][j-1]	
		
		if(left==nextc):
			print(left,i,j-1)
			found = search_pattern(char_list,idx+1, i,j-1, board)
			if(found):
				print("left found")
				return found
	board[i][j] = oldc
	return found


word = "AAB"
board = [["C","A","A"],
		 ["A","A","A"],
		 ["B","C","D"]]



  # ['A','B','C','E'],
  # ['S','F','C','S'],
  # ['A','D','E','E']]
m = len(board)
n = len(board[0])
print(m,n)
char_list = list(word)
print(char_list)
idx = 0
start_char = char_list[idx]

found = False

for i in range(0,m):
	if(found):
		break
	for j in range(0,n):
		print(i,j, board[i][j])
		if(start_char == board[i][j]):
			#print(start_char,i,j)
			if(idx+1==len(char_list)):
				found = True
				break	
			
			found = search_pattern(char_list, idx+1,i,j, board)
			#print("main loop:",found)
			if(found):
				break
print(found)














