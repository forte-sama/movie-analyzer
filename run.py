from src.movie_analyzer import format_movie_list, get_top_movies


if __name__ == "__main__":
    sample_raw_list = [
        [1, 9.3, "The Shawshank Redemption", True],
        [11, 7.5, "Star Wars: The Phantom Menace", False],
        [2, 9.2, "The Godfather", True],
        [3, 9.0, "The Dark Knight", True],
        [4, 8.8, "Pulp Fiction", True],
        [10, 8.7, "The Lord of the Rings: The Return of the King", True],
        [5, 8.5, "Inception", True],
        [6, 7.8, "Suicide Squad", False],
        [7, 9.1, "Schindler's List", True],
        [8, 8.2, "Interstellar", True],
        [15, 8.9, "Forrest Gump", True],
        [16, 7.9, "Joker", True],
        [9, 6.5, "Waterworld", False],
        [12, 8.4, "The Matrix", True],
        [13, 8.1, "Fight Club", True],
        [14, 5.9, "Cats (2019)", False],
        [17, 8.0, "The Grand Budapest Hotel", True],
        [18, 4.2, "Battlefield Earth", False]
    ]

    movie_list = format_movie_list(sample_raw_list)

    top_10 = get_top_movies(movie_list, top_n=10)
    print("Top 10 movies:")
    print(top_10)

    top_5 = get_top_movies(movie_list, top_n=5)
    print("Top 5 movies:")
    print(top_5)

    top_3 = get_top_movies(movie_list, top_n=3)
    print("Top 3 movies:")
    print(top_5)

    top_11 = get_top_movies(movie_list,
                            top_n=5,
                            condition_checker=lambda mov: mov.certified_fresh)
    print("Top 5 movies not certified fresh")
    print(top_11)
