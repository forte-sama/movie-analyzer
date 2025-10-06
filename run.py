from src.movie_analyzer import format_movie_list, get_top_movies, similar_movies


if __name__ == "__main__":
    sample_raw_list = [
        [1, 9.3, 'The Shawshank Redemption', True, ['DRAMA']],
        [2, 9.2, 'The Godfather', True, ['DRAMA', 'ACTION']],
        [3, 8.6, 'Parasite', True, ['DRAMA', 'THRILLER']],
        [4, 8.1, 'Mad Max: Fury Road', True, ['ACTION', 'ADVENTURE', 'SCI-FI']],
        [5, 9.0, 'The Dark Knight', True, ['ACTION', 'DRAMA']],
        [6, 8.8, 'Inception', True, ['SCI-FI', 'ACTION', 'ADVENTURE']],
        [7, 8.0, 'La La Land', True, ['ROMANCE', 'DRAMA', 'COMEDY']],
        [8, 3.7, 'The Room', False, ['DRAMA', 'ROMANCE']],
        [9, 5.2, 'Twilight', False, ['ROMANCE', 'FANTASY']],
        [10, 8.4, 'Avengers: Endgame', True, ['ACTION', 'ADVENTURE', 'SCI-FI']],
        [11, 8.5, 'Joker', True, ['DRAMA', 'THRILLER']],
        [12, 8.9, 'The Lion King', True, ['ADVENTURE', 'DRAMA']],
        [13, 4.1, 'The Last Airbender', False, ['ACTION', 'FANTASY', 'ADVENTURE']],
        [14, 8.7, 'Titanic', True, ['ROMANCE', 'DRAMA']],
        [15, 5.5, 'The Meg', False, ['ACTION', 'ADVENTURE']],
    ]

    movie_list = format_movie_list(sample_raw_list)

    top_10 = get_top_movies(movie_list, top_n=10)
    print("Top 10 movies:")
    print(top_10)

    top_10_like_this = similar_movies(movie_list, "Parasite", 8.1)
    print(top_10_like_this)

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
