- Assume a 5th column is added to this ingestion sheet that reports a genre.
  genre is a list that can contain any number of the following strings:
  `ACTION`, `DRAMA`, `COMEDY`, `ADVENTURE`, `SCI-FI`, `FANTASY`, `ROMANCE`.

## **How would we...**

Build a function `similar_movies(movie_title: str, rating: float | None)` that:

- Returns **top 10** movies similar genre.
- A rating that’s within a margin of 1 point the provided rating.
  - If rating is None, use the provided movie title’s rating.
