myParam = {\
	"server":"mpilgrim",\
	"database":"master",\
	"uid":"sa",\
	"pwd":"secret"\
}

print "myParam.items(): ", myParam.items(), " len: ", len(myParam.items())

key = [k for k,v in myParam.items()]
values = [v for k,v in myParam.items()]
keyValue = ["%s = %s" %(k,v) for k,v in myParam.items()]

print "myParam.key(): ", key, " len: ", len(key)
print "myParam.values(): ", values, " len: ", len(values)
print "myParam.keyValue(): ", keyValue, " len: ", len(keyValue)