"""
Uses Dijkstra's Algorithm to find the highest-cost route from row 0 to row 14
Rules: can only move from node (i, j) to (i+1, j) or (i+1, j+1) (i.e. 'down' the triangle)

"""

triangle =[
[75], #row 0 
[95, 64], 
[17, 47, 82], 
[18, 35, 87, 10], 
[20, 4, 82, 47, 65], 
[19, 1, 23, 75, 3, 34], 
[88, 2, 77, 73, 7, 63, 67], 
[99, 65, 4, 28, 6, 16, 70, 92], 
[41, 41, 26, 56, 83, 40, 80, 70, 33], 
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], 
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]] #row 14


ARBITRARILY_LARGE_NUMBER = 1000000
TRIANGLE_MAX = 1000 # a number larger than every number in 'triangle'

#invert each element in the triangle by subtracting it from TRIANGLE_MAX
#this is so the algorithm, in finding the lowest cost path, will actually find the highest cost path
for row in triangle:
    for i, term in enumerate(row):
        row[i] =  TRIANGLE_MAX - row[i]


#make a copy of 'triangle' but in the place of every number, put an empty list
#we will store the current minimum distance to each point here
path_lengths = [[ [] for number in row] for row in triangle]

#make another copy to store the lowest-cost path to each considered point
paths = [[ [] for number in row] for row in triangle]


# initialize distance storage. make the starting node of distance triangle[0][0],
# and the other nodes of arbitrarily high distance
for row in path_lengths:
    for i, term in enumerate(row):
        row[i] = ARBITRARILY_LARGE_NUMBER
path_lengths[0][0] = triangle[0][0]

#create a list of unvisited nodes
unvisited = [(i, j) for i in range(0, len(path_lengths)) for j in range(0, i+1)]


#'row' and 'col' are the coordinates of the current node
row = 0
col = 0

#until at the bottom, give the total cost to travel from the current node to all adjacent nodes
#there are only two adjacent nodes for every node (except those on final row have none)

while row < 14:
    
    #if the path to either of the adjacent nodes is shorter than a previous minimum,
    #replace the node's path and length with that of the lower-cost path,
    #and add the node to the end
    if path_lengths[row][col] + triangle[row+1][col] < path_lengths[row+1][col]:
        path_lengths[row+1][col] = path_lengths[row][col] + triangle[row+1][col]       
        paths[row+1][col] = paths[row][col] + [TRIANGLE_MAX - triangle[row][col]]
        
    if path_lengths[row][col] + triangle[row+1][col+1] < path_lengths[row+1][col+1]:
        path_lengths[row+1][col+1] = path_lengths[row][col] + triangle[row+1][col+1]
        paths[row+1][col+1] = paths[row][col] + [TRIANGLE_MAX - triangle[row][col]] #Using (TRIANGLE_MAX-<node>) 'de-inverts' the node
        
    #current node has been "visited"   
    unvisited.remove((row, col))
    
    min = ARBITRARILY_LARGE_NUMBER
    #visit the unvisited node with the lowest projected cost
    for (i, j) in unvisited:
        if path_lengths[i][j] < min:
            min = path_lengths[i][j]
            row = i
            col = j


paths[row][col] += [TRIANGLE_MAX - triangle[row][col]] #need to add last node to path
path_length = len(paths[row][col])
print "Path:", paths[row][col]
print "Max cost:", path_length * TRIANGLE_MAX - path_lengths[row][col] #'de-invert' the cost
