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



