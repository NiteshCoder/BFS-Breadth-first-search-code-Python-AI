
graph = {
	'A' : ['B' , 'C','D'],
	'B' : ['E'],
	'C' : ['F'],
	'D' : ['G'],
	'E' : [],
	'F' : ['Z'],
	'G' : [],
	'Z' : [],
}


visited = []
queue = []
final_result = [] 

def bfs(visited,graph,node):
	visited.append(node)
	queue.append(node)
	
	while queue:
		s = queue.pop(0)
		print(s,end=" ")
		#final_result.append(s)
		
		for neighbour in graph[s]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
	

bfs(visited,graph,'A')
print(final_result)	
