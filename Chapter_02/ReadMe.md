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

* A function does not define a return type nor its data type.
* A function declaration even does not inform if it returns any value.
    - In fact Python always returns value from a function, if not explicitly returned, it returns `None` by default.

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

## Documenting Function ##

Document the code is golden rule, and Python has this in its core, Python provides a way to document a Function as shown below.

````
def buildConnectionString(param):
    """ Build a connection string from a dictionary of parameters.
        Returns a String.
    """
````

EveryThing between the `""" """` triple quotes is a doc string, even the carriage returns and the New Line is preserved. We can use both the single and double quotes inside this triple quotes.

We can get this doc string by these two techniques, mentioned in a [StackOverflow question.](http://stackoverflow.com/questions/713138/getting-the-docstring-from-a-function)

````
example.buildConnectionString.__doc__

help(example.buildConnectionString)
````

In both the case, the output will be similar, but with a little formatting difference.

This Doc string can also be used as a ToolTip for IDE.

## Everything is an object ##

To prove that everything is an object in python, we will consider the function which we have already written, This function `buildConnectionString()` has attributes, one of the attributes which we have already seen is `buildConnectionString.__doc__`

To understand this, lets use the above function in a different manner as shown below.

````python
import example01
myParam = {\
    "server":"mpilgrim",\
    "database":"master",\
    "uid":"sa",\
    "pwd":"secret"\
}
print example01.buildConnectionString(myParam)
print example01.buildConnectionString.__doc__
````


Lets see the details of each line of code.

* The first line, `import `'s our existing file as a module. One a program is imported you can access any of its public functions, classes or attributes.
* To use methods, classes etc from the imported modules, we should use the format `moduleName.function `, in the above case `moduleName` := `example01 ` and `function ` : `buildConnectionString`
* Finally we invoked an attribute on the function `buildConnectionString` called `__doc__`.


