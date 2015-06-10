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





