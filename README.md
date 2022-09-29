# Nested Dictionary Database
Practice using recursive programming to define a nested dictionary that stores values in a way which makes evaluating weather a value is in the dictionary much faster.
# How It Works
Whenever a name is entered into the blank dictionary, another dictionary is created with the key of the first character of the name that contains another dictionary with the key of the second character and so on. When a new name is added to the database that shares the first few characters with another name previously entered, instead of creating a entire new set of nested dictionaries only dictionaries for the new set of charcters are made.
# Example
If you enter in "ab" as the first name and "ac" as the second, the database would contain one dictionary with a single key value pair of "a" and {"b":{"end":True},"c":{"end":True}}
(the end values simply signal that a name has finished with the charcter in the associated key)
