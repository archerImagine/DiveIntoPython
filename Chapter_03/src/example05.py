dictionary = {
	'server':'mpilgrim',
	'database':'pubs',
	"uid":'sa',
	'retrycount':3,
	42:'douglas'
}

print "dictionary : ", dictionary

del dictionary[42]
print "dictionary : ", dictionary

dictionary.clear()
print "dictionary : ", dictionary
