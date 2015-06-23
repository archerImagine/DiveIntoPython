print "'a' or 'b': ", 'a' or 'b'
print "'' or 'b': ", '' or 'b'
print "'a' or 'b' or 'c': ", 'a' or 'b' or 'c'
print "'' or [] or {} : ", '' or [] or {}

def sideFx():
	print "In sideFx()"
	return 1

print "'a' or sideFx(): ", 'a' or sideFx()