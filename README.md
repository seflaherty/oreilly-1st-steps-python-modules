# README - Python Modules and Packages from Agenda to actual Jupyter Lab Practice
**Presented by Reuven Lerner for O'Reilly Live Learning on April 1, 2021**

## What are modules?
**Takeaways**:
- Python libraries are called "modules"
- Because "it's a cracking good idea", these modules provide us with namespaces

## How do we `import` from a module into Python?
Let's cover module `random`:

The loading of modules is built into Python. It's not a function and we don't use parentheses with it.
```
import random
def foo():
    return f'{__name__} 4 you' # (szf) I see what you did there! -> 'main'
    # return f'foo.__name__ 4 you' # (szf) function `foo` has attribute name -> 'foo'


type(random)
<module 'random' from '/Users/sean/.pyenv/versions/3.9.2/lib/python3.9/random.py'>
type(foo)
<class 'function'>
```

Now do more stuff...

Get a list of attributes on an object with "dir"
`dir(random)`

Get help on module
`help(random)`

## An aside
**Naming Conventions**
* `myidentifier` this is a plain ol' variable or function -- all lowercase, public, etc.
* `MyBigName` this is in CamelCase, and should be a class.
* `__name__` this is "dunder name," and should be defined only if you know what Python expects to do with __name__ defined in your code.
* `_something` this is as private as things get in Python. Don't touch this in someone else's code.
* `something_` this is to avoid namespace collisions with things in Python.

## Different types of imports
- import from the standard library, like 'random'
- import from a distributed library, like 'requests'... for PyPi (the Python Package Index!)
- import your own module, like 'mymod', found in this repo

## Creating our own modules
- In the base directory, create 'mymod', 'mymod2', 'myprog'
- module 'mymod' imports standard library 'random', creates an int, list & dictionary vars, defines a function
- module 'mymod2' demonstrates DOCSTRING - an attribute of modules-, creates a dictionary var, defines a function
- module 'myprog' imports package `menustuff' (see below)
- use `importlib.reload(mymod)` :pointup, to iterate upon a module and force a reload

## Packages vs. modules
- In the base directory, create 'menustuff/', 'mypackage/'
    - Demo of the use of '__init__.py' to load more Python scripts (modules)
- Demo the common uses for `if __name__ == '__main__:`

### Importing modules from a package
1. `from PACKAGE import MODULE` - See that PACKAGE is not defined as a variable, but MODULE is.
2. `import PACKAGE.MODULE` - See that PACKAGE is defined as a variable, and MODULE is an attribute on that variable.
3. `import PACKAGE` - when there is a __init__.py file in the PACKAGE directory. In this case, __init__.py is executed, and is assigned the value of __file__. This file can define data and functions, and it can also import other modules... including modules in the current directory (with some syntactic sugar).

## `pip`
- install a PyPi package called `rich` that does a bunch of things, including colorizing our output from a Python script
- TBD: how about installing a better print? See [IceCream](https://github.com/gruns/icecream#icecream-in-other-languages)