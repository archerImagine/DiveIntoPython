li = ['Larry', 'Curly']
print "li.pop: ", li.pop
methodName = str(raw_input("Enter the Method to be invoked: "))
print getattr(li, methodName)
print "li: ", li