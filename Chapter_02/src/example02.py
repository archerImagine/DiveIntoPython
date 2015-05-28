import example01

myParam = {\
	"server":"mpilgrim",\
	"database":"master",\
	"uid":"sa",\
	"pwd":"secret"\
}

print example01.buildConnectionString(myParam)

print example01.buildConnectionString.__doc__