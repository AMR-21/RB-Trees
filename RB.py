class Node:
  def __init__(self,key):
    self.key = key
    self.parent = None
    self.right = None
    self.left = None
    self.red = True


class RBTree:
  def __init__(self):
    self.nil = Node(0)
    self.nil.red = False
    self.nil.right = None
    self.nil.left = None
    self.root = self.nil

  def rotateLeft(self, x):
    y = x.right
    x.right = y.left
    if y.left != self.nil:
      y.left.parent = x
    y.parent = x.parent
    if x.parent == None:
      self.root = y
    elif x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y    
    y.left = x
    x.parent = y  
    
  def rotateRight(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.nil:
        y.right.parent = x

    y.parent = x.parent
    if x.parent == None:
        self.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y  
    
  def insert(self, key):
    node = Node(key)
    node.red = True
    node.parent = None
    node.left = self.nil
    node.right = self.nil
    
    parent = None
    current = self.root
    
    while current != self.nil:
      parent = current
      if node.key < current.key:
        current = current.left
      elif node.key > current.key:
        current = current.right
      else:
        return    
    
    node.parent = parent
    if parent == None:
      self.root = node
    elif node.key < parent.key:
      parent.left = node
    else:
      parent.right = node    

    self.insertFixUp(node)
  
  def insertFixUp(self, node):
      while node != self.root and node.parent.red:
        #insertion of key in right subtree of the root
        if node.parent == node.parent.parent.right: 
          u = node.parent.parent.left
          #case 1
          if u.red: 
            u.red = False
            node.parent.red = False
            node.parent.parent.red = True
            node = node.parent.parent
          else:
            #case 2
            if node == node.parent.left:
              node = node.parent
              self.rotateRight(node)
            #case 3  
            node.parent.red = False
            node.parent.parent.red = True
            self.rotateLeft(node.parent.parent)    
        #insertion of key in left subtree of the root    
        else: 
          u = node.parent.parent.right
          #case 1
          if u.red: 
            u.red = False
            node.parent.red = False
            node.parent.parent.red = True
            node = node.parent.parent
          #case 2  
          else:
            if node == node.parent.right:
              node = node.parent
              self.rotateLeft(node)
            node.parent.red = False
            node.parent.parent.red = True
            self.rotateRight(node.parent.parent)  
      self.root.red = False        
  
  def search(self, key):
      current = self.root
      while current != self.nil:
        if key < current.key:
          current = current.left
        elif key > current.key:
          current = current.right
        else:
          return "Element with key {} exists".format(current.key)    
      return "Does not exist"  

  def height(self,n):
        if n == self.nil:
          return 0
        else:
          return 1 + max(self.height(n.right),self.height(n.left))

  def size(self,n):
        if n == self.nil:
          return 0
        else:
          return 1 + self.size(n.left) + self.size(n.right)
    
        