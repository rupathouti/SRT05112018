class Node:

  def __init__(self,data,nextNode=None):
    self.data = data
    self.nextNode = nextNode
  
  def getNextNode(self):
    return self.nextNode


class LinkedList:

  def __init__(self,head = None, tail = None):
    self.head = head
    self.tail = tail

  def AddToBack(self, data):
    # new_node = Node(data,self.head)
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
      new_node.nextNode= self.head
      self.head = new_node
    return True

  def PrintForward(self):
    curr_node = self.head
   
    while (curr_node != None):
      print(curr_node.data)
      curr_node = curr_node.getNextNode()

  def PrintReverse(self,curr_node):
    if (curr_node == None):
      return curr_node
    else:
      self.PrintReverse(curr_node.nextNode)
      print(curr_node.data)

  def PrintBackward(self):
    curr_node = self.head
    self.PrintReverse(curr_node)
    
    
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