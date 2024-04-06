class MultiStack:
    def __init__(self, stackSize):
        self.numberStackes = 3
        self.custList = [0] * (stackSize * self.numberStackes)
        self.size = [0] * self.numberStackes
        self.stackSize = stackSize

        print("self.numberStackes: ",self.numberStackes)
        print("self.custList: ",self.custList)
        print("self.size: ",self.size)
        print("self.stackSize: ",self.stackSize)
    
    def isFull(self, stackNum):
        print(" ")
        print("IsFull")
        print("*******************************************************")
        print("stackNum: "+str(stackNum))
        print("self.size[stackNum]: "+str(self.size[stackNum]))
        print("self.stackSize: "+str(self.stackSize))
        if self.size[stackNum] == self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self, stackNum):
        print(" ")
        print("isEmpty")
        print("*******************************************************")
        print("stackNum: "+str(stackNum))
        print("self.size[stackNum]: "+str(self.size[stackNum]))
        if self.size[stackNum] == 0:
            return True
        else:
            return False
        
    def indexOfTop(self, stackNum):
        print(" ")
        print("indexOfTop")
        print("*******************************************************")
        print("stackNum: "+str(stackNum))
        print("self.size[stackNum - 1]: "+str(self.size[stackNum - 1]))
        offset = stackNum * self.stackSize
        print("offset: "+str(offset ))
        print("offset + self.size[stackNum - 1]: "+str(offset + self.size[stackNum - 1]))
        return offset + self.size[stackNum - 1]
    
    def push(self, item, stackNum):
        print(" ")
        print("push")
        print("*******************************************************")
        if self.isFull(stackNum):
            return "The stack is full"
        else:
            self.size[stackNum] += 1
            print("************")
            print("self.size[stackNum]: ",self.size[stackNum])
            print("self.indexOfTop(stackNum): ",self.indexOfTop(stackNum))
            print("************")    
            self.custList[self.indexOfTop(stackNum)] = item
            print("self.custList: ",self.custList)


    def pop(self, stackNum):
        print(" ")
        print("pop")
        print("*******************************************************")
        if self.isEmpty(stackNum):
            return "Stack is Empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)]  
            self.custList[self.indexOfTop(stackNum)]  = 0
            self.size[stackNum] -= 1
            print("self.size[stackNum]: ",self.size[stackNum])
            print("self.indexOfTop(stackNum): ",self.indexOfTop(stackNum))
            print("self.custList: ",self.custList)
            print("value ",value)
            return value
        
    def peek(self, stackNum):
        print(" ")
        print("peek")
        print("*******************************************************")
        if self.isEmpty(stackNum):
            return "Stack is Empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)]  
            print("self.size[stackNum]: ",self.size[stackNum])
            print("self.indexOfTop(stackNum): ",self.indexOfTop(stackNum))
            print("self.custList: ",self.custList)
            print("value ",value)
            return value

custunStack = MultiStack(6)
print(custunStack.isFull(0))
print(custunStack.isEmpty(1))
custunStack.push(1,0)
custunStack.push(2,0)
custunStack.push(3,0)
custunStack.push(2,1)
custunStack.push(2,2)
custunStack.push(3,2)
print(custunStack.peek(1))

