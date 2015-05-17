# odbchelper.py

def buildConnectionString(param):
	"""	Build a connection string from a dictionary of parameters.
		Returns a String.
	"""
	return ";".join(["%s = %s" % (k, v) for k, v in param.items()])

if __name__ == '__main__':
	myParam = {\
	"server":"mpilgrim",\
	"database":"master",\
	"uid":"sa",\
	"pwd":"secret"\
	}
	print buildConnectionString(myParam)