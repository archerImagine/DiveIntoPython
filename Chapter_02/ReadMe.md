# Chapter 02 | The First Python Program. #

## Diving - In ##

Lets begin but simply copy pasting a source code from the book, which we will not understand upfront, but will dissect the code as we progress in the chapter.

````
# odbchelper.py

def buildConnectionString(param):
    """ Build a connection string from a dictionary of parameters.
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

````

If we run the above code, the O/P will be.

````
pwd = secret;database = master;uid = sa;server = mpilgrim
````

## Declaring Functions ##
