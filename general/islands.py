#HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" 
#(e.g. groups of connecting 1s)

def islands(Input): 
    #handle by cases- go right to left, top to bottom. If current 
    #element is 1, then it must either be: 
    #1. part of island above
    #2. part of island left 
    #3. both island above and left 
    #4. a new island 
    islandCounter = 0 
    assign = [] 
    for i in xrange(len(Input)):
        assign.append([]) 
        for j in xrange(len(Input[0])): 
            assign[i].append(0) 

    for i in xrange(len(Input[0])): 
        for j in xrange(len(Input)): 
            if Input[i][j] == 0: 
                continue #don't care about this element 
            if j != 0: #make sure we're not at top of Input array 
                top =assign[i][j-1] 
                if top != 0: 
                    assign[i][j] = top
            if i != 0:
                left = assign[i-1][j]
                if left != 0:
                    assign[i][j] = left 
            if assign[i][j] == 0  : #hasn't been assigned yet 
                islandCounter += 1 
                assign[i][j] = islandCounter
    
    print assign
    return islandCounter
d = [] 
d.append([0, 1, 0, 1, 1]) 
d.append([0, 1, 0, 1, 1]) 
d.append([0, 1, 0, 1, 1]) 
d.append([0, 1, 0, 1, 1]) 
d.append([0, 1, 0, 0, 0]) 

print islands(d)  #should be 1 
