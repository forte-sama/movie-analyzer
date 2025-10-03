from src.models.movie_model import Movie
from typing import List, Any, Iterable, Callable
import heapq

ConditionChecker = Callable[[Movie], bool]


def format_movie_list(raw_movie_list: Iterable[List[Any]]) -> List[Movie]:
    """
    Converts iterable of raw movie data into a list of Movie objects

    Args:
        raw_movie_list (Iterable[List[Any]]): 
            An iterable where each item is a list containing movie attributes (e.g., id, rating, movie_title, certified_fresh).

    Returns:
        List[Movie]: 
            A list of Movie objects created from raw_movie_list.
    """

    return [Movie(*row) for row in raw_movie_list]


def get_top_movies(movies: List[Movie],
                   top_n: int = 10,
                   condition_checker: ConditionChecker = lambda mov: mov.certified_fresh) -> List[Movie]:
    """
    Returns top N highest rated movies that meet the given condition.

    Returns top N highest rated movies that meet the given condition from the input list.
    Using a priority queue (min-heap) for optimal time complexity.

    Args:
        movies (List[Movie]): 
            List of movies to be searched upon.
        top_n (int): 
            Top N certified fresh movies wanted to be returned. Defaults to 10.
        condition_checker (Callable[[Movie], bool]): 
            Callable that checks for desired criteria. Defaults to look for movies with certified_fresh = True

    Returns:
        List[Movie]:
            Top N movies from the movies list.
    """

    sorted_movies = []

    # be safe around negative numbers
    top_n = max(0, top_n)

    for movie in movies:
        # let's just omit and not deal with the current movie if it does not meet the criteria
        if not condition_checker(movie):
            continue

        current_movie_tuple = (movie.rating, movie)

        if len(sorted_movies) < top_n:
            heapq.heappush(sorted_movies, current_movie_tuple)
        else:
            # get a hold of the worst movie kept
            min_rated_movie: Movie = sorted_movies[0][1]
            if movie.rating > min_rated_movie.rating:
                # remove worst movie and insert the better one
                heapq.heappushpop(sorted_movies, current_movie_tuple)

    # what was sorted was the list of tuples and a list of movies is the output
    top_movies = [mov_tuple[1] for mov_tuple in sorted_movies]

    # after the top n is guaranteed, the order based on ratings is not guaranteed, need to sort resulting list now
    top_movies.sort(key=lambda mov: mov.rating, reverse=True)

    return top_movies
