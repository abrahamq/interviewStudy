class node: 
    def __init__(self, value):
        self.left = None
        self.right = None 
        self.value = value 

    #inserts under this node 
    def insert(self, value): 
        if value > self.value: #go right 
            if self.right == None: #need to create the node 
                self.right = node(value)  
                return 
            else: 
                self.right.insert(value) 
        else: 
            if self.left == None: 
                self.left = node(value) 
                return 
            else: #keep looking for a place to put the value 
                self.left.insert(value) 
        return 

    #deletes an element from binary search tree 
    def delete(self, parent, value): 
        #if leaf, can just delete by removing link to parent 
        #if only one child, can just put that child under this one's parent 
        #if two children: delete(10) - replace 10 with successor, 12, then delete 12
        #    8 
        #  4   10
        #     9  12 
        if value > self.value:
            return self.right.delete(self, value) 
        elif value < self.value: 
            return self.left.delete(self, value) 

        if self.left == None and self.right == None: #delete leaf 
            if parent.right == self: 
                parent.right = None 
            else: 
                parent.left = None 
            return 
        #only one child 
        if self.left == None or self.right == None : 
            replace = self.left if self.left else self.right
            if parent.right == self: 
                parent.right = replace 
            else: 
                parent.left = replace
            return

        #two children: 
        #replace self with successor 
        successor = self.findMin()
        self.value = successor.value 
        #now delete successor
        successor.delete(self, successor.value) 
        return 

    #finds left most in subtree
    def findMin(self): 
        if self.left == None: 
            return self 
        return self.left.findMin() 


    def inOrderTraversal(self, process):
        if self.left != None: 
            self.left.inOrderTraversal(process)
        process(self.value)
        if self.right != None: 
            self.right.inOrderTraversal(process) 
        return 

res = [] 
def process(value): 
    res.append(value) 

root = node(10)

root.insert(5)
root.insert(15)
root.insert(11)

root.inOrderTraversal(process) 
#print res

res = []
root.delete(root, 10) 
root.inOrderTraversal(process) 
print res

