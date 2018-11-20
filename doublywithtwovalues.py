class Node:

    def __init__(self,data1,data2,nextNode=None,prevNode=None):
        self.data1 = data1
        self.data2 = data2
        self.nextNode = nextNode
        self.prevNode = prevNode

    def getNextNode(self):
        return self.nextNode

    def getPrevNode(self):
        return self.prevNode

class LinkedList:

    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail

    def AddToBack(self, data1,data2):
        if (self.head == None):
            new_node = Node(data1,data2)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data1,data2)
            new_node.prevNode = self.tail
            self.tail.nextNode = new_node
            self.tail = new_node
        return True


    def PrintForward(self):
        curr_node = self.head

        if self.head == None:
            print("linked list is empty")
    
        while curr_node != None:
            print(curr_node.data1),
            print("\b,"),
            print(curr_node.data2)
            # print(curr_node.data1, curr_node.data2)
            curr_node = curr_node.getNextNode()
  
    def PrintBackward(self):
        curr_node = self.tail

        if self.head == None:
            print("linked list is empty")
    
        while curr_node != None:
            print(curr_node.data1),
            print("\b,"),
            print(curr_node.data2)
            curr_node = curr_node.getPrevNode()

    def InsertAfter(self,data1,data2,new_data1,new_data2):
        curr_node = self.head

        while (curr_node != None):
            if curr_node.data1 == data1 and curr_node.data2 == data2:
                new_node = Node(new_data1,new_data2, self.head)
                new_node.nextNode = curr_node.nextNode
                new_node.prevNode = curr_node

                curr_node.nextNode = new_node
                curr_node.nextNode.prevNode = curr_node

                break

            curr_node = curr_node.getNextNode()

        
    def InsertBefore(self,data1,data2,new_data1,new_data2):
        curr_node = self.head
        while curr_node != None:
            if curr_node.data1 == data1 and curr_node.data2 == data2:
                new_node = Node(new_data1,new_data2)
                new_node.prevNode = curr_node.prevNode
                new_node.nextNode = curr_node
                curr_node.prevNode.nextNode = new_node
                curr_node.prevNode = new_node 
        
                break
      
            curr_node = curr_node.getNextNode()
    
    def ReplaceValue(self,data1,data2,new_data1,new_data2):
        curr_node = self.head

        while curr_node != None:
            if curr_node.data1 == data1 and curr_node.data2 == data2:
                curr_node.data1 = new_data1
                curr_node.data2 = new_data2
            curr_node = curr_node.getNextNode()

    def ReplaceAtPos(self,pos,new_data1,new_data2):
        curr_node = self.head
        index = 1
        if pos == 1:
            self.head.data1 = new_data1
            self.head.data2 = new_data2
            return True
        else:
            while curr_node != None: 
                if index == pos:
                    curr_node.data1 = new_data1
                    self.head.data2 = new_data2
                    return True

                curr_node = curr_node.getNextNode()
                index = index + 1

        print("Position does not exist in the linked list")
        return False

    def InsertAtPos(self,pos,new_data1,new_data2):
        curr_node = self.head
        index = 1
    
        while curr_node != None: 
            if pos == 1:
                new_node = Node(new_data1,new_data2)
                new_node.prevNode = None
                new_node.nextNode = curr_node
                curr_node.prevNode = new_node
                self.head = new_node
                return True

            elif index == pos:
                new_node = Node(new_data1,new_data2)
                new_node.prevNode = curr_node.prevNode
                new_node.nextNode = curr_node
                curr_node.prevNode.nextNode = new_node
                curr_node.prevNode = new_node
                return True

            curr_node = curr_node.getNextNode()
            index = index+1

        print("Position does not exist in the linked list")
        return False

    def Removeatfront(self): 
        if (self.head != None): 
            self.head = self.head.nextNode
        else:
            print("linked list is empty")

    def Removeatend(self):
        if self.head == None:
            print("linked list is empty")
        elif self.head.nextNode == None:
            self.head = None
            self.tail = None
        else: 
            self.tail.prevNode.nextNode = None
            self.tail = self.tail.prevNode

    def Removeatpos(self,pos):
        curr_node = self.head
        index = 1
        if self.head == None:
            print("linked list is empty")
    
        else:
            while curr_node != None: 
                if pos == 1:
                    self.head = self.head.nextNode
                    return True
                elif index == pos: 
                    curr_node.prevNode.nextNode = curr_node.nextNode
                    curr_node.nextNode.prevNode = curr_node.prevNode
                    return True       
        
                curr_node = curr_node.getNextNode()
                index = index+1

            print("Position exceeded the list")
            return False

myList = LinkedList()
myList.AddToBack(2,3)
myList.AddToBack(5,6)
myList.AddToBack(20,30)
myList.AddToBack(8,9)
print("Printing forward now")
myList.PrintForward()
myList.Removeatpos(3) 
print("********************")
myList.PrintForward()