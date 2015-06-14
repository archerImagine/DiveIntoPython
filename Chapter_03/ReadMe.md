# Chapter 03 | Native DataTypes. #
There are 3 major native DataTypes.

* Dictionaries
* Tuples
* List.

## Introducing Dictionaries ##
This is a built-in data types in python. This defines a one-to-one relationship between keys and value.

### Defining Dictionaries ###

A dictionary can be defined by:-

````python
dictionary = {
    'server':'mpilgrim',
    'database':'master'
}

print "dictionary: ", dictionary
````
The above code creates a new Dictionary, with 2 elements in it.Each Element is a key-value pair.
This will print 

````python
dictionary:  {'database': 'master', 'server': 'mpilgrim'}
````
Some operation which we can do with Dictionaries.

* We can retrieve the value of a key with this notation, `dictionary['server']`, will return `mpilgrim`.
* We can retrieve value based on Key, but not the other way around, `dictionary['mpilgrim']`, this raises a error called `KeyError`

### Modifying Dictionaries ###

Here are some operation on the sample dictionary which we already have named `dictionary `.

* `dictionary['database'] = "pubs"`
    - We cannot have duplicate entry in a dictionary, so when assigning value to a existing key will replace the value.
* `dictionary['uid'] = "sa"`
    - We can add a key-Value pair at anytime. The syntax is same as modifying existing key's value.
* One important concepts to remember about Dictionary is, They do not have a order of storing elements, or Key-Value pair.
* Dictionary keys are case sensitive.
    - So `d['key'] = "value"` is different from `d['Key'] = "third Value."`
* Dictionary can have different data types, not just strings.
    - Dictionary **values** can be integers, string, objects, or even other dictionary.
    - Dictionary **Key** are more restrictive, they can be strings, integers and few others, basically it should be immutable.

### Deleting Items from Dictionary ###

Consider the below example:-

````python
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
````
* We can delete a particular element of the dictionary, by using its key as shown here.
    - `del dictionary[42]`
* We can also remove all the elements with the help of `clear()` method of dictionary, but the empty dictionary will still remain.
    - `dictionary.clear()`

## Introducing Lists. ##
A list is more like a array in some other languages, but capable of holding heterogeneous elements in it. `ArrayList` of Java comes close to a List.

A list has these properties.

* A list is dynamic, i.e. it can be updated anytime.
* It can hold any type of objects in it.

### Defining List ###

We can define a list as shown below.

````python
li = ['a', 'b', 'mpilgrim', 'z', 'examples']
````

Since a List is like an array we can also do index based operation on the list, and just like some arrays, the list's index begins at `0`.

So here are some examples to access the list.

````python
print li[0]     # prints 'a'
print li[4]     # prints 'examples'
````

Since the index is a number we can also use **negative index**, when we use negative index, it just subtracts that number from the length of the list and gives the element at that index.

````python
print li[-3]     # prints 'mpilgrim' length of list = 5, so 5 - 3 = 2, li[2] = 'mpilgrim'
print li[-1]     # prints 'examples', length of list = 5, so 5 - 1 = 4, li[4] = 'example'
````

### Slicing a list ###

We can always get a sub list from the actual list. This sublist is called **Slice**. This done by suppling two indices. The return values is a new list, containing elements from the first slice index, upto the second index, not including it.

let see some example:-

````python
li = ['a', 'b', 'mpilgrim', 'z', 'examples']

print "li[1:3] : ", li[1:3]         # prints ['b', 'mpilgrim']
print "li[1:-1] : ", li[1:-1]       # prints ['b', 'mpilgrim', 'z']
print "li[0:3] : ", li[0:3]         # prints ['a', 'b', 'mpilgrim']
````

This is how slicing can be understood.

* While reading the list from left to right, the first slice index tells us about the first element which we want, and the second slice index tells us the first element which you do not want.

Some short hand about slice.

* if any of the slice has to start at `0` index, you can leave the index, ex. `li[:3]` = `li[0:3]`
* similarly if the slice has to extend till the last element. `li[3:]` = `li[3:5]`
    - On important thing to note is if we do a slice like these 
        + `li[:n]` - Will return the first n elements.
        + `li[n:]` - Will return the rest.
* If we want complete slice of the list, `li[:]`

### Adding Element to the list. ###
Here are some Apis from List, which we can use to add elements to the list.

* `append()`
    - `li.append('new')` : this is add the element `new` at the end of the list `li`
* `insert()`
    - `li.insert(2,'new') ` : this will add the element `new ` at the index `2` in the list `li`
    - We can have duplicate elements in a list.
* `extend()`
    - `li.extend(['two', 'element'])` : `extend()` takes a single argument which is a list, and it concatenates the argument list with `li`

Now we might see, what is the difference between `append()` and `extend()`
Here is a example of `extend()`

````python
li = ['a','b','c']
li.extend(['d','e','f'])
print "li = ", li, " len(li) = ", len(li), " li[-1] = ", li[-1]
````

* `extend()`
    - `extend ` takes a single arguments which is a list, and adds each of the elements to the original list.
    - In the above example, the final list will have 6 elements.


Here is an example of `append()`
````python
li = ['a','b','c']
li.append(['d','e','f'])
print "li = ", li, " len(li) = ", len(li), " li[-1] = ", li[-1]
````
* `append()`
    - `append()` also takes one arguments, though not restricted only to list.
    - It simply adds it to the end of the original list.
    - Now as we see in the above example, we have a final list with 4 elements, because we appended a list itself not elements of the list.

### Searching Lists. ###

We can search for a element in a list with `index ` function and also `in` operator.

````python
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'examples', 'new', 'two', 'element']

print "li.index('examples'): ", li.index('examples')
print "li.index('new'): ", li.index('new')
print '"c" in li : ', "c" in li

print "li.index('c'): ", li.index('c')
````

* `index()`
    - It finds the first occurrence of an element, so in case of `index('new')`, it will return 2, though we have another `"new"`.
    - If a value is not found, it raise a `ValueError.`
    - To test if a element is in a list or not we use the `in` operator.

### Deleting list elements ###

Here is an example of Deleting list elements:-

````python
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'examples', 'new', 'two', 'element']
print "Original Li = ", li

print "li.remove('z') : ", li.remove('z'), "li: ", li
print "li.remove('new') : ", li.remove('new'), "li: ", li
print "li.pop() : ", li.pop(), "li: ", li
print "li.remove('c') : ", li.remove('c'), "li: ", li
````
* `remove()`
    - `remove()`, removes the first matching elements from the list.
    - `remove()`, just like `index()` raises a `ValueError` if we invoke it with arguments which is not present in the list.
* `pop()`
    - It removes the last element from the list, and returns that element.

### Using List Operators ###

* A list can be concatenated using `+` operator which is similar to `extend()`
* `+=` also has the same behavior as `+`
* `*` works as a list repeater.

Here is an example:-

````python
li = ['a', 'b', 'mpilgrim']
print "li = ", li

li = li + ['example', 'new']
print "After adding ['example', 'new'], li = ", li

li += ['two']
print "After adding ['two'], li = ", li

li = [1, 2] * 3
print "li = ", li
````

## Introducing Tuple ##

A Tuple is a immutable list.A tuple cannot be changes once it is created.

A tuple is defines exactly like a list, with just the exception that we use `()` brackets.

````python
t =('a','b','mpilgrim','z','example')
print "t[0]: ", t[0]
print "t[-1]: ", t[-1]
print "t[1:3]: ", t[1:3]
````

* Tuple also have a order just like list, and they are 0 indexed.
* Negative index, counts from the end of the list.
* Slicing is also same as list.
* Tuple have no methods.
* We cannot add, remove, find element in a tuple.
* We can check for presence of an element in a tuple with use of `in` operator.

So with so many disadvantages with is the real advantages of tuples.

* Tuples are very fast.
* It is one way to make anything write protected.
* Dictionary can have tuple as a key but not list, even with tuple, these tuple cannot be keys. Any tuple with can be considered unsafe cannot be the key.
    - A tuple of list.


## Declaring Variables. ##

Python has both global and local variables, but they do not have an explicit declaration. Variables comes into existence when they are assigned values, and destroyed when they go out of scope.

Here is an example of variable declaration:-

````python
if __name__ == '__main__':
    myParam = {\
    "server":"mpilgrim",\
    "database":"master",\
    "uid":"sa",\
    "pwd":"secret"\
    }
````

As shown above, we have a variable declared as `myParam`, so when we use line continuation character, `\`, the next line can be indented as we wish, there is not hard bound on the formating.

Expression within brackets, any form can be split over multiple line with out taking care of the indentation.

We cannot reference a variable till we have assigned value to it, it raise a error `NameError`.

We can also assign multiple values at once in python. This is shown below.

````python
v = ('a','b','c','d')
print "v = ", v

(x,y,z,u) = v
print "x = ", x, " y = ", y, " z = ", z, " u = ", u
````

We can also get the functionality of `enum `s in C in python, by doing this.

`(MONDAY,TUESDAY,WEDNESDAY,THRUSDAY,FRIDAY,SATURDAY,SUNDAY) = range(7)`

We can use this concept of tuple been returned in function to return multiple values, which we can then assign to same variable or multiple variable.


## Formatting Strings ##

Python supports formatting values to string. There can be very complicated uses case for this, but the most simplest use is by the `%` operator.

Here is an example for the same.

````python
k = 'uid'
v = 'sa'

print "%s = %s" %(k,v)  # Prints uid = sa
````

The string `"%s = %s" %(k, v)` is what we will concentrate, the first `%s` gets its value from `k` in the tuple `(k, v)`, and the second `%s`, gets its value from `v`.

The above is a example of [type coercion ](https://tapestry.apache.org/type-coercion.html).

The above case of string formating might look like a little too much which can be simply achieved by string concatenation. This is not the case, consider the below example.

````python
uid = "sa"
pwd = "secret"

print pwd + " is not a good password for " +uid
print "%s is not a good password for %s" %(pwd,uid)

userCount = 6
print "User Connected %d" %(userCount, )
print "User Connected " +userCount
````

Everything is fine when we are using string, but once we have an integer, all hell break loose if we use the `+` operator, as it gives a type error `TypeError: cannot concatenate 'str' and 'int' objects`

So the String formating using the `%` operator is far more than just string concatenation. It can work with floats, integers and strings.

So here are the strings which should follow `%` for different data types.

| string | Value    |
| :----: | :----    |
| `s`    | strings  |
| `d`    | integers |
| `f`    | float    |

## Mapping List ##

If there is any feature in Python, which makes me fall in love with it, its is List Comprehension or Mapping List.

List Comprehension provides a way of mapping a list into another list, by applying a function on each of the element of original list.

Here is an example of list comprehension in action.

````python
li = [1, 9, 8, 4]
print "li = ", li

print [elem*2 for elem in li]

li = [elem*2 for elem in li]
print "li = ", li
````

To understand this expression `[elem*2 for elem in li]`, we should start for right to left.
* `for elem in li`, this takes each element from `li` and puts the value in `elem`
* `elem*2` for each element `elem` we multiply it by `2` and store it in the new list.

Few Points about List Comprehension.
* List Comprehension does not modify the original list.
* We can even assign the List Comprehension output to the original list, because the new list is created in memory, and once the complete list is created it will be assigned to original list, so we will not reach a infinite loop.

We can also use List Comprehension on Dictionary not only limited to List. Consider the `buildConnectionString()` and in particular this line, `["%s = %s" % (k, v) for k, v in param.items()]`

So before we understand the above code, we have to understand these methods of dictionary.

* `keys()`
    - The `keys` method of a dictionary returns a list of all the keys of dictionary. The list is not in the order in which the dictionary was defined.
* `values()`
    - The `values` method of a dictionary returns a list of all the values of dictionary. The list is in order of return of `keys`, so we can say `param.values()[n] == param[param.keyes()[n]]`
* `items()`
    - The `items` method of a dictionary returns a list of the form `(key, value)`. 

To understand we can see the below code.

````python
myParam = {\
    "server":"mpilgrim",\
    "database":"master",\
    "uid":"sa",\
    "pwd":"secret"\
}

print "myParam.keys() = ", myParam.keys()
print "myParam.values() = ", myParam.values()
print "myParam.items() = ", myParam.items()
````

This is the output:- 

````python
myParam.keys() =  ['pwd', 'database', 'uid', 'server']
myParam.values() =  ['secret', 'master', 'sa', 'mpilgrim']
myParam.items() =  [('pwd', 'secret'), ('database', 'master'), ('uid', 'sa'), ('server', 'mpilgrim')]
````

Here is a step by step process of what we try to achieve in this line of code.

* `["%s = %s" % (k, v) for k, v in param.items()]`

````python
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
````

## Joining List and splitting Strings ##

We can join each element of a list, using a delimiter, by the use of `join()` method.

Here is the most simplest example:-

````python
li = ['a','b','c','d']
print ";".join(li)      # prints a;b;c;d
````

Similarly if we look into the `buildConnectionString` function we will find this code:-

* `";".join(["%s = %s" % (k, v) for k, v in param.items()])`

So `";"` is a string object and we are invoking the `join()` method on it.

Similar to joining element of a list, we also have a `split ` method, which will split a string into a list using a delimiter.

Here is the example for performing both `join()` and `split()`

````python
li = ['pwd = secret', 'database = master', 'uid = sa', 'server = mpilgrim']
s = ";".join(li)
print "String = ", s
liNew = s.split(";")
print "liNew: ", liNew
````

* `split()` has an optional argument which is a integer, which tells how many splits to performs.
