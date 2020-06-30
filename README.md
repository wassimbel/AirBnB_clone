# airbnb clone
run ./console.py to start the command interpreter.

# usage:

# create:
*Creates a new instance of BaseModel
*saves it(to the JSON file) and prints the id
*Ex$ create BaseModel

# show:
*Prints the string representation of an instance
*EX$ show BaseModel 1234-1234-1234.

# destroy:
*Deletes an instance based on the class name and id
(save the change into the JSON file)
*EX$ destroy BaseModel 1234-1234-1234.

# all:
*Prints all string representation of all instances
*Ex$ all BaseModel or $ all.

# update:
*Updates an instance based on the class name and id
*EX$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
