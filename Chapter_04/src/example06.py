import os, __builtin__
li = []
print "Len: ", len(dir(li)), " dir(li): ", dir(li)

d = {}
print "Len: ", len(dir(d)), " dir(d): ", dir(d)

print "Len: ", len(dir(os)), " dir(os): ", dir(os)

print "Len: ", len(dir(__builtin__)), " dir(__builtin__): ", dir(__builtin__)