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








