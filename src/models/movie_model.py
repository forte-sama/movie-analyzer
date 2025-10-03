from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    id: int
    rating: float
    movie_title: str
    certified_fresh: bool = False
