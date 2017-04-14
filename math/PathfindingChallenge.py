#this program uses Dijkstra's Algorithm to find the highest-cost route from row 0 to row 14
#rules: can only move from node (i, j) to (i+1, j) or (i+1, j+1) (i.e. 'down' the pyramid)
#if your python installation is good, should print 1074

array =[
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

#invert each element in the array (99 is max)
#this is so the algorithm, in finding the lowest cost path, will actually find the highest cost path
for i in range(0,len(array)):
    for j in range(0,len(array[i])):
        array[i][j] =  99 - array[i][j]

#this is where the current minimum distance to each point will be stored
distances =[
[[]],
[[],[]],
[[],[],[]],
[[],[],[],[]],
[[],[],[],[],[]],
[[],[],[],[],[],[]],
[[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]


#this is where the lowest-cost path to each considered point will be stored
paths = [
[[]],
[[],[]],
[[],[],[]],
[[],[],[],[]],
[[],[],[],[],[]],
[[],[],[],[],[],[]],
[[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]

#initialize distance storage. make the starting node of value 24 (99 - 75) and the other nodes of arbitrarily high cost
distances[0][0] = 99-75
for i in range(1, len(distances)):
    for j in range(0, len(distances[i])):
        distances[i][j] =  1000000

#create a list of unvisited nodes
unvisited = [(i, j) for i in range(0, len(distances)) for j in range(0,i + 1)]

#'row' and 'col' are the coordinates of the current node
row = 0
col = 0
while row < 14:
    #until at the bottom, give the total cost to travel from the current node to all adjacent nodes
    #there are only two adjacent nodes for every node (except those on final row have none)
    
    if distances[row][col] + array[row+1][col] < distances[row+1][col]:
        distances[row+1][col] = distances[row][col] + array[row+1][col]
            #replace the node's path with the lower-cost path
        paths[row+1][col] = paths[row][col] + [99 - array[row][col]]
            #paths[row][col] is path to current node, 100-array[row][col] is name of current node
            #i.e., the path to the next node is the path to the current node, plus the current node
        
    if distances[row][col] + array[row+1][col+1] < distances[row+1][col+1]:
        distances[row+1][col+1] = distances[row][col] + array[row+1][col+1]
        paths[row+1][col+1] = paths[row][col] + [99 - array[row][col]] #Using '99 - node' de-inverts the node's name
        
    #current node has been "visited"   
    unvisited.remove((row, col))
    
    min = 10000000
    #visit the unvisited node with the lowest projected cost
    for (i, j) in unvisited:
        if distances[i][j] < min:
            min = distances[i][j]
            row = i
            col = j
    
print "Max cost:", 99*len(distances) - distances[row][col]
paths[row][col] += [99 - array[row][col]] #need to add last node to path
print "Path:", paths[row][col]

#this is an Euler challenge but I thought the solution was neat enough to post
