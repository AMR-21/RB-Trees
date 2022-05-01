from RB import RBTree as tree


  
list = [41, 38, 31, 12, 19, 8]

t1 = tree()
for i in range(0,len(list)):
    t1.insert(list[i])      

print(t1.search(413))
print(t1.height(t1.root))   
print(t1.size(t1.root)) 