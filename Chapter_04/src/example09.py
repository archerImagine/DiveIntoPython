li = ['Larry', 'Curly']
print "li.pop: ", li.pop
print "getattr(li, 'pop') : ", getattr(li, 'pop')
print "Append Using getattr: ", getattr(li,'append')('Moe')
print "li: ", li

print 'getattr({},"clear"):', getattr({},"clear")
print 'getattr((),"clear"):', getattr((),"clear")