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
