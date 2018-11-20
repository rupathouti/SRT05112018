class Node:

  def __init__(self,data,nextNode=None,prevNode=None):
    self.data = data
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

  def AddToBack(self, data):
    if (self.head == None):
      new_node = Node(data)
      self.head = new_node
      self.tail = new_node
    else:
      new_node = Node(data)
      new_node.prevNode = self.tail
      self.tail.nextNode = new_node
      self.tail = new_node
    return True

  def AddToFront(self, data):
    if (self.head == None):
      new_node = Node(data)
      
      self.head = new_node
      self.tail = new_node
    else:
      new_node = Node(data, self.head)
      self.head.prevNode = new_node
      new_node.nextNode = self.head
      self.head = new_node
    return True

  def PrintForward(self):
    curr_node = self.head

    if self.head == None:
      print("linked list is empty")
    else:
      while curr_node != None:
        print(curr_node.data)
        curr_node = curr_node.getNextNode()
  
  def PrintBackward(self):
    curr_node = self.tail

    if self.head == None:
      print("linked list is empty")
    else:
      while curr_node != None:
        print(curr_node.data)
        curr_node = curr_node.getPrevNode()
    
  def InsertAfter(self,data,new_data):
    curr_node = self.head

    while (curr_node != None):
      if ((curr_node.data) == data):
        new_node = Node(new_data, self.head)
        new_node.nextNode = curr_node.nextNode
        new_node.prevNode = curr_node

        curr_node.nextNode = new_node
        curr_node.nextNode.prevNode = curr_node

        break

      curr_node = curr_node.getNextNode()

    print("Value after which you need to insert is not exist in list")
    return False

  def InsertBefore(self,data,new_data):
    curr_node = self.head
    while curr_node != None:
      if curr_node.data == data:
        new_node = Node(new_data)
        new_node.prevNode = curr_node.prevNode
        new_node.nextNode = curr_node
        curr_node.prevNode.nextNode = new_node
        curr_node.prevNode = new_node 
        
        break
      
      curr_node = curr_node.getNextNode()
    
    print("Value after which you need to insert is not exist in list")
    return False

  def ReplaceValue(self,data,new_data):
    curr_node = self.head

    while curr_node != None:
      if (curr_node.data == data):
        curr_node.data = new_data
        #If you want to replace only first data in list then you need to write break
      curr_node = curr_node.getNextNode() #Replaces all the similar values in the linked list
    
  def ReplaceAtPos(self,pos,new_data):
    curr_node = self.head
    index = 1
    if pos == 1:
      self.head.data = new_data
      return True
    else:
      while curr_node != None: 
        if index == pos:
          curr_node.data = new_data
          return True

        curr_node = curr_node.getNextNode()
        index = index + 1

    print("Position does not exist in the linked list")
    return False


  def InsertAtPos(self,pos,new_data):
    curr_node = self.head
    index = 1
    
    while curr_node != None: 
      if pos == 1:
        new_node = Node(new_data)
        new_node.prevNode = None
        new_node.nextNode = curr_node
        curr_node.prevNode = new_node
        self.head = new_node
        return True

      elif index == pos:
        new_node = Node(new_data)
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

myList.AddToBack(5)
myList.AddToBack(7)
myList.AddToBack(1)
myList.AddToBack(10)
myList.AddToBack(11)
myList.AddToBack(7)
myList.AddToBack(10)
myList.PrintForward() 
print("***********************")
myList.ReplaceValue(10,99)
myList.PrintForward() 