#these are examples of 12 commands, I'm considering doing a movie database.  :D
import easygui
import os

easygui.msgbox("Welcome to the Python Movie Recommendation Tool!", "Welcome")

choice = easygui.buttonbox("What would you like to do?",
                           choices=["Open Movie File", "View Random Recommendation", "Exit"])

if choice == "Open Movie File":
    movie_file = easygui.fileopenbox("Select a movie file (txt format)", filetypes=["*.txt"])

    if movie_file:
        user_name = easygui.enterbox("Enter your name", "User Info")

        genres = easygui.multenterbox("Enter your favorite genres", "Preferences", ["Genre 1", "Genre 2", "Genre 3"])

        with open(movie_file, "r") as f:
            movies = f.read().splitlines()
        selected_movie = easygui.choicebox("Select a movie to save as your favorite", "Movie Picker", movies)

        easygui.msgbox(f"You selected {selected_movie} as your favorite!", "Selection Confirmed")

        save_file = easygui.filesavebox("Save your favorite movie list", default="favorites.txt", filetypes=["*.txt"])
        if save_file:
            with open(save_file, "w") as f:
                f.write(f"{user_name}'s Favorite Movie: {selected_movie}\n")
                f.write("Favorite Genres: " + ", ".join(genres) + "\n")

        folder = easygui.diropenbox("Choose a folder to save additional movie info")
        if folder:
            easygui.msgbox(f"Extra movie info can be saved in {folder}", "Folder Chosen")

        if easygui.ynbox("Do you want a random movie recommendation?", "Random Recommendation"):
            import random

            random_movie = random.choice(movies)
            easygui.msgbox(f"We recommend you watch: {random_movie}", "Random Movie")

            poster_path = easygui.fileopenbox("Select an image file for the movie poster", filetypes=["*.png", "*.jpg"])
            if poster_path:
                easygui.imagebox(poster_path, f"{random_movie} Poster")

        fav_movies = easygui.multchoicebox("Select other favorite movies", "Favorites", movies)
        if fav_movies:
            easygui.msgbox(f"Your favorite movies list: {', '.join(fav_movies)}", "Favorites List")

else:
    easygui.msgbox("Thanks for using the Movie Recommendation Tool!", "Goodbye")
