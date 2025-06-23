ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# ft_list is a list: a list contains comma-separated items enclosed in brackets. 
# These items can have different types, but usually they are of the same type.
# Lists are mutable, it is possible to change, add, or remove their content.

ft_list[1] = "World!"

#t_tuple is a tuple: a tuple contains comma-separated items enclosed in parentheses. These items can have different types.
#Tuples are immutable — it is impossible to change their content after creation.
#However, it is possible to duplicate a tuple or create a new one based on an existing one.

ft_tuple = (ft_tuple[0], "France!")


# ft_set is a set: a set contains comma-separated unique items enclosed in curly braces.
# These items can be of different types, but sets cannot contain duplicates.
# Sets are mutable, so it is possible to add or remove items after creation.

ft_set.remove("tutu!")
ft_set.add("Paris!")

# ft_dict is a dictionary: a dictionary contains comma-separated key-value pairs enclosed in curly braces.
# Each key is unique and maps to a value.
# Dictionaries are mutable, so you can add, modify, or remove key-value pairs.

ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
