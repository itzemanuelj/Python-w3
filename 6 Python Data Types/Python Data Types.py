''' Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

## Getting the Data Type

print(type("2"))

## string

print(type(2))
## int

x = "Hello Wolrd" ## str

x = 1 ## int

x = 1.0 ## float

x = 1j ##comlex

x = ["apple", "apple", "apple", "apple"] ## list

x = ("apple", "apple", "apple", "apple") ## tuple  

x = range(4) ##range 


## Setting the Specific Data Type

x = str("Hello World") ## str

x = int(1) ## int

x = float(1.0) ## float

## x = {"name": justin, "age": 28} ## dict

x = {"appple", "bannana", "cherry"}  ## set

x = frozenset({"apple", "banana", "cherry"})	## frozenset

x = True ##bool

x = b"Hello"	##bytes

x = bytearray(5)	##byterry

x = memoryview(bytes(5))	##memorybite

x = None ## nonetype












