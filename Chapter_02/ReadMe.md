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

Python simplicity can be just understood from the way a function is declared. There is no fuss of have a header file like C++ or being a *interface/ implementation* like Pascal.

This is how a python function is declared, with some of its special property.

````
def buildConnectionString(param):
````

* `def` is the keyword to start the function declaration.
* Followed by the function name.
* In brackets we have arguments, if we have multiple arguments these are comma separated.

If you see the code to declare properly, you will notice that there is no return type defined. A few property of return type in python.

* A function does not define a return type not its data type.
* A function declaration even does not inform if it returns any value.
    - In face Python always returns value from a function, if not explicitly returned, it returns `None` by default.

Few differences from other programming languages.

* Python does not have a sub routines unlike VB.
* The arguments are never typed.    

### Python Data types Compared to other programming languages. ###

Basically there are these 4 type of languages.

* Statically Typed Language.
    - This type of languages fixes the data type of a variable during compile time. This is enforced by most languages by enforcing variables to have a data type. **Java**, **C**, **C++** are such languages.
* Dynamically Typed Language.
    - In these type of languages, the data type of a variables is identified during the run time execution. **VBScript**, **Python** are such languages.
* Strongly Typed Language.
    - A Languages in which types are always enforced, i.e. once a variable is defined a `int` it cannot be changed automatically to a string. **Java** and **Python** are two such languages.
* Weakly Typed Language.
    - A Language where type can be ignored at any time, like **VBScript.**

So **Python** is

* Dynamically Typed Language &
* Strongly Typed Languages.
