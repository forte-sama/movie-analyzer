from src.models.movie_model import Movie
from typing import List, Any, Iterable


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
