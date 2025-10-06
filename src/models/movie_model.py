from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Movie:
    id: int
    rating: float
    movie_title: str
    certified_fresh: bool
    genres: List[str]
