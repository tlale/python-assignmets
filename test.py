# my_dictionary = {
#     "first": "John",
#     "last": "Doe",
#     "city": "New York",
#     "year": 2023,
#     "average": 100
# }
# print(my_dictionary["first"])
# car = dict(brand='Toyota', model='Camry', year=2022)
# print(car["brand"])

# keys = ['a', 'b', 'c']
# values = ["A for Apple", "B for banana", "C for Cat"]
# my_dict = dict(zip(keys, values))
# print(my_dict["a"])

# sample_dict = {"java" : 1, "python" : 2, "nodejs" : 3}
# sample_dict.update( nodejs = 2 )
# print(sample_dict)
# sample_dict.update( python = 3 )
# print(sample_dict)

# books = {'Fluent Python':50, 'Learning Python':58}
# more_books = {'Effective Python':40, 'Think Python':29}
# books.update(more_books)
# print(books) 
# Create a dictionary to store learner information.
# my_dict = {
#     "first": "John",
#     "last": "Doe",
#     "city": "New York",
#     "year": 2023,
#     "average": 100
# }

# Add a new key:value pair to the dictionary.
# my_dict["age"] = 36

# # Update an existing value within the dictionary.
# my_dict["year"] = 2022

# Delete a value from the dictionary.
# del my_dict["average"]

# # Print the modified dictionary.
# print(my_dict)
# print(my_dict.get("first"))  # Output: John
# print(my_dict.get("age")) 
# my_keys = my_dict.keys()
# print(my_keys)      # output: dict_keys([‘first’, ‘last’, ‘city’, ‘year’, ‘average’])

#tupples as dictionary keys
fruit_colors = {( 'apple', 'banana'): 'yellow', ('cherry', 'date'): 'red'}
print(fruit_colors[('apple', 'banana')])
