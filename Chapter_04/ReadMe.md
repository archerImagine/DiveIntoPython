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


## Using `type `, `str`, `dir ` and other Built-in Function. ##
Python by design have a very limited built-in function, rest all functions are packaged into modules. This decision was mainly not to bloat the core language.

### The `type ` Function ###

The `type ` function returns the data type of any arbitrary object. All the possible types are listed in `types` modules.

Consider the below example.


````python
import os,types

print "type(1): ", type(1)
print "type([]): ", type([])
print "type(os): ", type(os)
print "type(os) == types.ModuleType : ", type(os) == types.ModuleType
````

* `type ` can take any type of object.

### The `str` Function ###
The `str` function coerces data into string.

Consider the below example:-

````python
import os

print "str(1): ", str(1)
horsemen = ['war', 'pestilence', 'famine']
horsemen.append('PowerBuilder')
print "str(horsemen): "+ str(horsemen)
print "str(os): ", str(os)
print "str(None): ", str(None)
````
### The `dir ` Function ###

The `dir ` returns a list of attributes and methods of any objects, modules, functions, strings, lists, dictionary.

Consider the below example:-

````python
import os
li = []
print "Len: ", len(dir(li)), " dir(li): ", dir(li)
d = {}
print "Len: ", len(dir(d)), " dir(d): ", dir(d)
print "Len: ", len(dir(os)), " dir(os): ", dir(os)
````
* `dir` returns a list with the name of the methods, not the actual methods.
* `dir` when applied on modules, will return these property
    - built-in attribute.
    - methods.



### The `callable ` function. ###
The `callable ` function take any object and returns `True ` if the object can be called.

Here is an example of the same.

````python
import string

print "string.punctuation: ", string.punctuation, " callable(string.punctuation) : ", callable(string.punctuation)
print "string.join: ", string.join, " callable(string.join) : ", callable(string.join)
````

### Built-In Function ###

These functions which we have discussed till now and few more are grouped into a special module called `__builtin__`.

* `type `
* `str`
* `dir`


We can assume that python automatically executes `from __builtin__ import *` on startup.

## Getting Object reference with `getattr` ##
All functions in Python are objects. An important property of the function which can be used is, we can get a reference of a function without knowing its name until run-time by using `getattr ` function.

Here are some example of `getattr() `.

````python
li = ['Larry', 'Curly']
print "li.pop: ", li.pop
print "getattr(li, 'pop') : ", getattr(li, 'pop')
print "Append Using getattr: ", getattr(li,'append')('Moe')
print "li: ", li

print 'getattr({},"clear"):', getattr({},"clear")
print 'getattr((),"clear"):', getattr((),"clear")
````

Now it will be very difficult to consume the above example, because we already know that list has a `pop ` method, and we pass the same `"pop" ` string in `getattr`, then what is the value add We are getting by using `getattr `?

The answer to this will be simple.

Lets say, we are taking input from user, for what methods to invoke on `li`. Consider the below example:-

````python
li = ['Larry', 'Curly']
print "li.pop: ", li.pop
methodName = str(raw_input("Enter the Method to be invoked: "))
print getattr(li, methodName)
print "li: ", li
````

Now the `methodName` will not be known in advance to the program, and also it will be a string object, on which we cannot invoke the method.

If you are a C programmer, associate the `getattr` with function pointers.

### `getattr ` as a dispatcher ###

The best example of `getattr ` is that of a dispatcher. Consider the below example.

If we have a program, which outputs its results in different formats, We can write different function to give output in different formats, and then use a single dispatch function `getattr` to execute the function.

So to extend the above example, lets say we have 3 methods.

* `ouput_html() ` : Outputs the result in html.
* `output_xml() ` : Outputs the result in xml.
* `output_text() ` : Plain text output.

Now in which format to output is dependent on any of these:-

* Command Line parameters.
* Configuration file.

So lets understand this by code.

````python
# example01
def output_html():
    print "Printing in html..."

def output_xml():
    print "Printing in xml..."  

def output_text():
    print "Printing in text..."
````

````python
import example01

def output(data, format='text'):
    output_function = getattr(example12,'output_%s' %format)
    return output_function()

if __name__ == '__main__':  
    format = str(raw_input("Enter the output format: "))
    output("hello", format)
````
Now, we have two files, `example01` defines all the output format function, and we import this in another file, and when we run this program, it ask's the user for a output format, which is then converted to string and passed to `getattr`.

If we did not had `getattr`, we would have written a dictionary to map all the keys to a function, or would have written multiple if else statement.

Now there is a bug in the above code, suppose the user enters `ads` as an input, no we do not have a `output_ads` method in example01, and so it will raise a `AttributeError`.

To solve this problem we can pass a default output type in `getattr`, which will be used, if the user does not passes a correct value.

`output_function = getattr(example12,'output_%s' %format, example01.output_text)`

## Filtering List ##

Python has a powerful capability of creating one list from another called list comprehension. This list comprehension can also have a filtering mechanism in which we do not select every element from original list to process.

The general structure will look like this.

* `[mapping-expression for element in source-list if filter-expression]`

The first 2/3 part is already known to us, the only difference if from the `if` code. The filter-expression when evaluated to `True` will save the element in the new list.

Consider the below for understanding the filtering concept.

````python
li = ['a','mpilgrim','foo','b','c','b','d','d']
print "li", li

newList = [elem for elem in li if len(elem) > 1]
print "newList", newList

newList = [elem for elem in li if elem != 'b']
print "newList", newList

newList = [elem for elem in li if li.count(elem) == 1]
print "newList", newList
````

We have different `if` statement in the above code, which acts as a filter.

* The first if, filters out any element whose length is > 1.
* The second if, filters out element which do not begin with `b`
* The last if is interesting, because it uses the list's count method, to remove duplicate from the original list. It not only remove the duplicate it even does not have a single entry of the duplicates in the new list.

So now we are in a position to understand this piece of code from the first example.

* `methodList = [method for method in dir(object) if callable(getattr(object, method))]`


So here are the steps which is performed in the above line of code.

1. `object ` is passed as a input to this.
2. We find all the attributes and methods 

## The peculiar Nature of `and` and `or` ##
In Python, `and` and `or` provide the logic operation, but the peculiar thing about the operation is that, it returns one of the value under the operation and not just a boolean value.

When using `and` or `or` values are evaluated in boolean context, as a reason of this, `0`, `''`, `{}`, `()`, `[]` and `None` evaluates to false. 

When using class, the object of a class is by default `True`, but we have some methods which can change the behavior to return `False`.

Consider the below example for `and` :-

* `'a' and 'b'`
    - if all values are `True ` in boolean context, then `and` returns the last value.
* `'' and 'b'`
    - if any value is `False ` in boolean context, then `and` returns the first value.

Consider the below example for `or` :-

* `'a' or 'b'` 
    - In case of `or` it evaluates from left to right and returns the value which is the first `True ` in the sequence.
* `'' or [] or {}`
    - If all values are `False `, `or` returns the last value. In above case it returns `{}`.
* `or` evaluates only till it gets the first `True ` value so, if we have an expression or function after the `True ` value it will never gets executed.


### Using the `and-or` Trick ###

## Using `lambda ` Expression ##

### Real World `lambda ` Expression ###

## Putting it together. ##

## Summary ##






