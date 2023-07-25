class node:
  def __init__(self,data):
    self.data=data
    self.next=None

class linked_list:
  def __init__(self):
    self.head=None

  def show(self):
    if self.head is None:
      print("linked list is empty!")
    else:
      temp=self.head
      while temp is not None:
        print(temp.data,"--->",end=" ")
        temp=temp.next

  def add_begin(self,new_data):
    new_node=node(new_data)
    new_node.next=self.head
    self.head=new_node

  def insert_empty(self,new_data):
    if self.head is None:
      new_node=node(new_data)
      self.head=new_node
    else:
      print("linked list is not empty!")

  def add_mid__after(self,mid,new_data):
    temp=self.head
    while temp is not None:
      if temp.data==mid:
        break
      temp=temp.next
    if temp is None:
      print("node not present in linked list")
    else:
      new_node=node(new_data)
      new_node.next=temp.next
      temp.next=new_node

  def add_mid_before(self,mid,new_data):
    temp=self.head
    while temp.next is not None:
      if temp.next.data==mid:
        break
      temp=temp.next
    if temp.next is None:
      print("node not present in linkedlist")
    else:
      new_node=node(new_data)
      new_node.next=temp.next
      temp.next=new_node

  def add_end(self,new_data):
    new_node=node(new_data)
    if self.head is None:
      self.head=new_node
    else:
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      temp.next=new_node

  def delete_begin(self):
    if self.head is None:
      print("linked list is empty,we can't delete any values")
    else:
      self.head=self.head.next

  def delete_end(self):
    if self.head is None:
      print("linked list is empty,we can't delete any values")
    elif self.head.next is None:
        self.head=None
    else:
      temp=self.head
      while temp.next.next is not None:
        temp=temp.next
      temp.next=None

  def delete_by_value(self,remove_node):
    if self.head is None:
      print("linked list is empty!")
      return
    if self.head.data==remove_node:
      self.head=self.head.next
      return
    temp=self.head
    while temp.next is not None:
      if remove_node==temp.next.data:
        break
      temp=temp.next
    if temp.next is None:
      print("node not present")
    else:
      temp.next=temp.next.next

l1=linked_list()
# insert on empty list and list adding funcs
print("---------------------------------------------------------------------------------")
l1.show()
print("---------------------------------------------------------------------------------")
print("\n\n------------------------------after insert empty---------------------------------")
l1.insert_empty(0)
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n------------------------------after insert end-----------------------------------")
l1.add_end(1)
l1.add_end(4)
l1.add_end(6)
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n------------------------------add mid after--------------------------------------")
l1.add_mid__after(4,5)
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n------------------------------add mid before-------------------------------------")
l1.add_mid_before(4,3)
l1.add_mid_before(3,2)
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n------------------------------add begin------------------------------------------")
l1.add_begin(-1)
l1.add_begin(-2)
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n---------------------------------delete begin------------------------------------")
l1.delete_begin()
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n---------------------------------delete end---------------------------------------")
l1.delete_end()
l1.show()
print("\n---------------------------------------------------------------------------------")
print("\n\n---------------------------------delete by value----------------------------------")
l1.delete_by_value(3)
l1.show()
print("\n---------------------------------------------------------------------------------")
