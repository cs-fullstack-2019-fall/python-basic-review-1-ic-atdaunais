def main():
    # season = "Fall"
    # print(f"My favorite season is {season}!!")
    # myLoop()
    # select_movie()
    # userInput = int(input("Enter the grade you received: "))
    # print(user_grade(userInput))
    # list_loop()
    my_games()


def myLoop():
    liftoff_counter = 10
    while liftoff_counter > 0:
        print(liftoff_counter)
        liftoff_counter -= 1
    print("LIFTOFF!!!")


def select_movie():
    movie1 = "Moonlight"
    movie2 = "My Neighbor Totoro"
    movie3 = "August Rush"
    movie_list = [movie1, movie2, movie3]
    for eachMovie in movie_list:
        print(f"{movie_list.index(eachMovie)}. {eachMovie}")
    movie_pick = int(input("Which movie is your favorite from the list? Enter the correct index number: "))
    if movie_pick == 0:
        print(f"You selected {movie_list[movie_pick]}")
    elif movie_pick == 1:
        print(f"You selected {movie_list[movie_pick]}")
    elif movie_pick == 2:
        print(f"You selected {movie_list[movie_pick]}")


def user_grade(grade):
    if grade > 100 or grade < 0:
        return "Invalid grade"
    elif grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    elif grade <= 59:
        return "F"


def list_loop():
    game_wish_list = ['CyberPunk', 'Borderlands 3', 'Break the Game']
    for eachGame in game_wish_list:
        print(eachGame)
    game_wish_list.append(input("Please enter a game you would like to add to the list: "))
    for eachGame in game_wish_list:
        print(eachGame)


def my_games():
    class Game:
        def __init__(self, name, release_year, rating):
            self.name = name
            self.release_year = release_year
            self.rating = rating

        def update_rating(self):
            choose_game = int(input("Enter the index of the game you want to change: "))
            if choose_game == 0:
                user_rate = int(input("Enter a new rating for the game(1-5): "))
                game1.rating = user_rate
                print(f"The rating of the game {game1.name} is now {game1.rating}.")
            if choose_game == 1:
                user_rate = int(input("Enter a new rating for the game(1-5): "))
                game2.rating = user_rate
                print(f"The rating of the game {game2.name} is now {game2.rating}.")
            if choose_game == 2:
                user_rate = int(input("Enter a new rating for the game(1-5): "))
                game3.rating = user_rate
                print(f"The rating of the game {game3.name} is now {game3.rating}.")

        def __str__(self):
            return f"Name:          {self.name}\n" \
                   f"Release year:  {self.release_year}\n" \
                   f"Game Rating:   {self.rating}\n"

    game1 = Game("Ocarina of Time", "1998", 5)
    game2 = Game("Baba Is You", "2019", 4)
    game3 = Game("Shadow of the Colossus", "2005", 5)
    game_collection = [game1, game2, game3]

    for eachGame in game_collection:
        print(eachGame)

    game1.update_rating()

    for eachGame in game_collection:
        print(eachGame)


main()
