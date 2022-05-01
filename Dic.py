from main import Node as node
from main import RBTrees as RBtree

class Dictionary:
  def __init__(self,path):
    self.path = path
    self.load()
  
  def load(self):
    with open("EN-US-Dictionary.txt","r",encoding="UTF-8") as f:
      self.lines=f.readlines()
  
  def size(self):
    return len(self.lines)
  
  def insert(self,key):
    pass 
  
  def lookUP(self,key):
    pass
    