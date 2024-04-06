import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:   #--------------------------->o(1)
        return
    print(rootNode.data)   #----------------------->o(1)                    Time Complecity : O(n)
    preOrderTraversal(rootNode.leftChild)   #------>o(n/2)                  Space Complecity : O(n)
    preOrderTraversal(rootNode.rightChild)  #------>o(n/2)


# ------------------------------------------------------------------
    

def inOrderTraversal(rootNode):
    if not rootNode:   #--------------------------->o(1)
        return                                                             
    inOrderTraversal(rootNode.leftChild)   #------->o(n/2)                  Time Complecity : O(n)
    print(rootNode.data)   #----------------------->o(1)                   Space Complecity : O(n)
    inOrderTraversal(rootNode.rightChild)  #------->o(n/2)
   

# ------------------------------------------------------------------
    
    
def postOrderTraversal(rootNode):
    if not rootNode:   #--------------------------->o(1)
        return
    postOrderTraversal(rootNode.leftChild)   #----->o(n/2)                 Time Complecity : O(n)
    postOrderTraversal(rootNode.rightChild)  #----->o(n/2)                 Space Complecity : O(n)
    print(rootNode.data)   #----------------------->o(1)                    
   
   

# ------------------------------------------------------------------
    
    
def levelOrderTraversal(rootNode):
    if not rootNode:     #---------------------------------------->o(1)
        return
    else:
        customQueue = queue.Queue()  #---------------------------->o(1)
        customQueue.enqueue(rootNode)  #-------------------------->o(1)         Time Complecity : O(n)
        while not(customQueue.isEmpty()):  #---------------------->o(n)         Space Complecity : O(n)
            root = customQueue.dequeue()  #----------------------->o(1)
            print(root.value.data)
            if (root.value.leftChild is not None):  #------------->o(1)
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None): #------------->o(1)
                customQueue.enqueue(root.value.rightChild)


# ------------------------------------------------------------------
    

def searchBT(rootNode, nodeValue):
    if not rootNode:  #------------------------------------------->o(1)
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()  #---------------------------->o(1)
        customQueue.enqueue(rootNode)  #-------------------------->o(1)
        while not(customQueue.isEmpty()):  #---------------------->o(n)          Time Complecity : O(n)
            root = customQueue.dequeue()  #----------------------->o(1)          Space Complecity : O(n)
            if root.value.data == nodeValue:   #------------------>o(1)
                return "Success"
            if (root.value.leftChild is not None):  #------------->o(1)
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):  #------------->o(1)
                customQueue.enqueue(root.value.rightChild)
        return "Not found"


# ------------------------------------------------------------------
    
    
def insertNodeBT(rootNode, newNode):
    if not rootNode:  #------------------------------------------->o(1)
        rootNode = newNode
    else:
        customQueue = queue.Queue()  #---------------------------->o(1)
        customQueue.enqueue(rootNode)  #-------------------------->o(1) 
        while not(customQueue.isEmpty()):  #---------------------->o(n)
            root = customQueue.dequeue()  #----------------------->o(1)         Time Complecity : O(n)
            if root.value.leftChild is not None: #---------------->o(1)         Space Complecity : O(n)
                customQueue.enqueue(root.value.leftChild)                       
            else:                          #---------------------->o(1)
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:  #-------------->o(1)
                customQueue.enqueue(root.value.rightChild)
            else:                           #--------------------->o(1)
                root.value.rightChild = newNode
                return "Successfully Inserted"


# ------------------------------------------------------------------
    
    
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode


# ------------------------------------------------------------------
    
    
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


# ------------------------------------------------------------------
    
    
def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"


# ------------------------------------------------------------------
    
    
def deleteBT(rootNode):
    rootNode.data = None  #-------------------->o(1)                Time Complecity : O(1)
    rootNode.leftChild = None  #--------------->o(1)                Space Complecity : O(1)
    rootNode.rightChild = None  #-------------->o(1)
    return "The BT has been successfully deleted" 

levelOrderTraversal(newBT)

# preOrderTraversal(newBT)

        
            





