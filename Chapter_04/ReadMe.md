# Chapter 04 | The Power of Introspection #

## Dive In ##

Like [Chapter 02 | The First Python Program ](../Chapter_02/ReadMe.md), lets start with a full source code of a program first.

````python
def info(object,spacing=10, collapse=1):
    """
        Prints methods and doc Strings.
        Takes Modules, class, list, dictionary, or string.
    """
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %(method.ljust(spacing),
                                processFunc(str(getattr(object, method).__doc__))) 
                                for method in methodList])
if __name__ == '__main__':  
    print info.__doc__
````

Now everything might not be clear at a first instance, lets try to understand some part of it.

* `def info(object,spacing=10, collapse=1):`
    - This function declaration looks weird in the first glance, we understood it needs 3 arguments, `object `, `spacing `, `collapse `, The last 2 have a little different syntax, for now just think these 2 as something called **Optional arguments**.
* The body of the function, will be understood by the time we finish this chapter.

To use the above function we call use it like this.

````python
li = []

info(li)
````

This will print all the function available in the `li` objects.


## Optional and Named Arguments. ##
Python has two different ways of accessing a arguments to a Function.

* Optional Arguments.
    - Python allows arguments to have default values, like we saw in `def info(object,spacing=10, collapse=1):` in this, `spacing=10` is a default values, so if while calling `info()` we do not pass the value of `spacing `, it will take the default value of `10`, same is the case with `collapse `.
* Named Arguments.
    - In Python, we can pass arguments in any order, so it does not matter if we know the sequence of arguments in a function call, we can still call the function.

Lets understand in more details Named and Optional arguments with the function definition of `info`

````python
def info(object,spacing=10, collapse=1):
````

* `spacing ` and `collapse ` are optional arguments, so if we call `info` with just one argument, `info` will take the default value of `spacing ` & `collapse `.
* If we call `info` with 2 arguments, then `collapse ` gets the default value of `1`.
* If we have to pass 2 arguments to `info`, that of `object ` and `collapse `, and it should take the default value of `spacing `, in other language, this will be impossible, but in Python it is possible with the help of named arguments, We can call like this `info(myObject, collapse = 0)`.
* For required arguments, if we use named arguments, then the order does not matter else it matters.

The above concepts, looks very different, but once you realize that the function arguments is just a dictionary, then all of this makes real sense.