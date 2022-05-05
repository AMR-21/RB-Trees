from RB import RBTree as Tree

class Dictionary:
  def __init__(self,path):
    self.path = path
    self.tree = Tree()
  
  def load(self):
    with open(self.path,"r",encoding="UTF-8") as f:
      self.lines=f.readlines()
    for line in self.lines:
      self.tree.insert(line.casefold()) 
  
  def size(self):
    return self.tree.size(self.tree.root)
  
  def insert(self,key):
    exist = self.tree.search(key)
    if exist:
      return 'Error: Word already in the dictionary'
    self.tree.insert(key)
    return 'Inserted Successfully'
    
    
  def lookUP(self,key):
    return self.tree.search(key)
    