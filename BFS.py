#!/usr/bin/env python

#Breadth-First Search from MIT OpenCourseWare:
#https://www.youtube.com/watch?v=s-CYnVz-uh4

def BFS(s, Adj):
	level = {s: 0} #Dictionary : specifies key value pairs
	parent = {s: None}
	i = 1
	frontier = [s] #<- level i - 1 (everything you reached last iteration)
	while frontier:
		next = [] #<- all the things you can reach in i moves
		for u in frontier:
			for v in Adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append(v)
	frontier = next
	i += 1