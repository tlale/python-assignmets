
import keyword
import json
import os
 
# Define dictionary of movies and their information
movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}

# Print out the movies and their information using square bracket syntax and .keys and .values
for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

# Update an element in the dictionary
movies["The Dark Knight"]["year"] = 2009

# Delete an element from the dictionary
del movies["Pulp Fiction"]

# Get a value from the dictionary using .get
genre = movies.get("Inception").get("genre")
print(f"The genre of Inception is {genre}.")

# add a new movie
def add_movies():
    title = input("enter movie tile: ")
    
    if title in movies:
        print('Movie already exist.')
        return
    
    try:
     year = int(input('Enter release Year: '))
    except ValueError:
       print('Year must be a number. ') 
       return

genre = input("Enter genre: ")
director = input("Enter director: ")
title = input("Enter movie title:")
actors = input("Enter actors (comma separated): ").split(",")

movies[title] = {
        #"year": year,
        "genre": genre,
        "director": director,
        "actors": [actor.strip() for actor in actors]
    }

print("Movie added successfully.")

#edit a movie
def edit_movie():
    title = input("Enter movie title to edit: ")

    if title not in movies:
        print("Movie not found.")
        return
    
    movies[title]["genre"] = input("New genre: ")
    movies[title]["director"] = input("New director: ")

    actors = input("New actors (comma separated): ")
    movies[title]["actors"] = [actor.strip() for actor in actors.split(",")]

    print('Successfully added a movie')

    #delete a movie
    def delete_movie():
     title = input("Enter movie title to delete: ")

    if title in movies:
        del movies[title]
        print("Movie is deleted.")
    else:
        print("Movie not found.") 

        #search for a movie
    def search_movie():
     search = input("Enter a title, genre, director, year or actor: ").lower()

    found = False

    for title, info in movies.items():

        if (search in title.lower() or
            search == str(info["year"]) or
            search in info["genre"].lower() or
            search in info["director"].lower() or
            any(search in actor.lower() for actor in info["actors"])):

            print(title)
            print(info)
    #         found = True

    # if not found:
    #     print("Movie not found.") 
    #     def search_movie():
    #      search = input("Enter a title, genre, director, year or actor: ").lower()

    # found = False

    # for title, info in movies.items():

    #     if (search in title.lower() or
    #         search == str(info["year"]) or
    #         search in info["genre"].lower() or
    #         search in info["director"].lower() or
    #         any(search in actor.lower() for actor in info["actors"])):

    #         print(title)
    #         print(info)
    #         found = True

    # if not found:
    #     print("Movie not found.")
#     def search_movie():
#         search = input("Enter a title, genre, director, year or actor: ").lower()

# for title, info in movies.items():
#     if (search in title.lower() or
#         search == str(info["year"]) or
#         search in info["genre"].lower() or
#         search in info["director"].lower() or
#         any(search in actor.lower() for actor in info["actors"])):
#         print(title)
#      search = input("Enter title, genre, director, year or actor: ").lower()

#     found = False
# for title, info in movies.items():

#    if (search in title.lower() or
#             search== str(info["year"]) or
#             search in info["genre"].lower() or
#             search in info["director"].lower() or
#             any(search in actor.lower() for actor in info["actors"])):

#           print("\nMovie:", title)
#           print(info)
#     found = True

# if not found:
#     print('No matching movie found')          

    #save data
    def save_movies():
        with open('movies.json', 'w') as file:
             json.dump(movies, file, indent=4)

        print('Movies Successfully Saved')

        #load data
        def load_movies():
            global movies

    try:
        with open("movies.json", "r") as file:
            movies = json.load(file)

        print("Movies loaded successfully.")

    except FileNotFoundError:
        print("No saved file found.")


        #movie menu
        while True:

         print("\n===== Movie Database =====")
        print("1. View Movies")
        print("2. Add Movie")
        print("3. Edit Movie")
        print("4. Delete Movie")
        print("5. Search Movie")
        print("6. Save Movies")
        print("7. Load Movies")
        print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_movies()

    elif choice == "2":
        add_movie()

    elif choice == "3":
        edit_movie()

    elif choice == "4":
        delete_movie()

    elif choice == "5":
        search_movie()

    elif choice == "6":
        save_movies()