class Node:

  def __init__(self,data,nextNode=None):
    self.data = data
    self.nextNode = nextNode
  
  def getNextNode(self):
    return self.nextNode

  def getPrevNode(self):
    return self.prevNode

class LinkedList:

  def __init__(self,head = None, tail = None):
    self.head = head
    self.tail = tail

  def insertAt(self, prevNode, data): 
  
    if (prevNode == None): 
      print "The given previous node must inLinkedList."
      return
    new_node = Node(data) 
  
    new_node.nextNode = prevNode.getNextNode
  
    prevNode.nextNode = new_node 

  def AddToBack(self, data):
    if (self.head == None):
      new_node = Node(data,self.head)
      self.head = new_node
      self.tail = new_node
    else:
      new_node = Node(data)
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
      self.head = new_node
    return True

  def PrintForward(self):
    curr_node = self.head
    # list_items = []
    while curr_node != None:
      print(curr_node.data)
      # list_items.append(curr_node.data)
      curr_node = curr_node.getNextNode()

    # for item in list_items:
    #   print(item)

    

  def PrintBackward(self):
    if (self.head == None):
      return
    PrintBackward(head.getNextNode)
    print(self.head.data)
    # curr_node = self.head
    # list_items = []
    # while curr_node != None:
      # list_items.append(curr_node.data)
      # curr_node = curr_node.getNextNode()

    # for item in list_items[::-1]:
    #   print(item)
    
  def Removeatfront(self): 
  
    if self.head != None: 
      self.head = self.head.nextNode


  def Removeatend(self): 
    if self.head != None:
      if self.head.nextNode == None:
        self.head = None
      else:
        curr_node = self.head
        while curr_node.nextNode.nextNode != None:
          curr_node = curr_node.getNextNode()
        curr_node.nextNode = None
    # if self.head != None: 
    #   self.head = self.head.nextNode
    # else:
    #   temp = temp.nextNode
    
    #   nextNode = temp.nextNode.nextNode
  
    #   temp.nextNode = None
    #   temp.nextNode = nextNode 

myList = LinkedList()

myList.AddToBack(5)
myList.AddToBack(7)
myList.AddToBack(1)
myList.AddToBack(10)
myList.AddToBack(11)
print("Printing forward now")
myList.PrintForward() 
# print("Printing backward now")
# myList.PrintBackward()
print("****")
myList.insertAt(1,10)
# myList.Removeatfront()
# myList.Removeatend()
print("****")

myList.PrintForward() 








