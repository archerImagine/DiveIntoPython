li = ['a','mpilgrim','foo','b','c','b','d','d']
print "li", li

newList = [elem for elem in li if len(elem) > 1]
print "newList", newList

newList = [elem for elem in li if elem != 'b']
print "newList", newList

newList = [elem for elem in li if li.count(elem) == 1]
print "newList", newList