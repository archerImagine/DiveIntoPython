li = ['a','b','c','d']
print ";".join(li)

li = ['pwd = secret', 'database = master', 'uid = sa', 'server = mpilgrim']
s = ";".join(li)
print "String = ", s
liNew = s.split(";")
print "liNew: ", liNew, " len(liNew): ", len(liNew)

LiNext = s.split(";",1)
print "LiNext: ", LiNext, " len(LiNext): ", len(LiNext)