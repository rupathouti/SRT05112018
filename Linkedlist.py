class Node:

  def __init__(self,data,nextNode=None):
    self.data = data
    self.nextNode = nextNode
  
  def getNextNode(self):
    return self.nextNode

  # def getPrevNode(self):
  #   return self.prevNode

class LinkedList:

  def __init__(self,head = None, tail = None):
    self.head = head
    self.tail = tail

  # def insertAt(self, prevNode, data): 
  
  #   if (prevNode == None): 
  #     print "The given previous node must inLinkedList."
  #     return
  #   new_node = Node(data) 
  
  #   new_node.nextNode = prevNode.getNextNode
  
  #   prevNode.nextNode = new_node 
  def get_no_of_nodes(self):
    curr_node = self.head

    no_of_nodes = 0
    
    while curr_node != None:
      curr_node = curr_node.getNextNode()
      no_of_nodes = no_of_nodes + 1

    return no_of_nodes

  def InsertAt(self,position,new_data):
    if (position <= self.get_no_of_nodes() + 1):
      curr_node = self.head


      temp_pos = 1
      while temp_pos != position:
        curr_node =  curr_node.getNextNode()
        temp_pos = temp_pos + 1

      new_node = Node(new_data, self.head)

      new_node.nextNode = curr_node.nextNode
      new_node.prevNode = curr_node

      curr_node.nextNode = new_node
      curr_node.nextNode.prevNode = curr_node

    else:
      print("There is no given position in the given Doubly Linked list")
      
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
    self.PrintReverse(self.head)
    
    

  # def PrintBackward(self):
  #   if (self.head == None):
  #     return
  #   new_node = Node(data)
  #   new_node.reverse(head.getNextNode)
  #   print(self.head.data)
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


  def PrintReverse(self,currentNode): 
    if currentNode == None:#Checking for ta
      return
    self.PrintReverse(currentNode.getNextNode())
    print(currentNode.data)

  def Removeatend(self): 
    if self.head != None:
      if self.head.nextNode == None:
        self.head = None
      else:
        curr_node = self.head
        while curr_node.nextNode.nextNode != None:
          curr_node = curr_node.getNextNode()
        curr_node.nextNode = None
    

myList = LinkedList()

myList.AddToBack(5)
myList.AddToBack(7)
myList.AddToBack(1)
myList.AddToBack(10)
myList.AddToBack(11)
print("Printing forward now")
myList.PrintForward() 
print("Printing backward now")

myList.PrintBackward()
#myList.PrintBackward(myList.head)
print("****")
# myList.insertAt(1,10)
# myList.Removeatfront()
# myList.Removeatend()
# print("****")

# myList.PrintForward() 