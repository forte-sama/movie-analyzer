import pytest
from src.movie_analyzer import Movie, format_movie_list, get_top_movies

# dummy raw data
MOVIE_DATA = [
    [11, 9.5, 'Hereditary', True],
    [20, 7.0, 'Weapons', True],
    [10, 9.9, 'Signs', True],
    [13, 8.5, '28 Days Later', False],  # not fresh
    [54, 8.8, 'Midsommar', True],
    [90, 7.5, 'The Rite', True],
    [71, 9.0, 'A Quiet Place', True],
    [44, 6.0, 'Evil Dead Rise', False],  # not Fresh
    [99, 9.1, 'The Conjuring', True],
]


def test_format_list_with_invalid_row():
    raw_data = [
        *MOVIE_DATA,
        [101, 1, 'Dalmatians'],
        [1, 3.5, 'Yes Man'],
        [2, 'The Truman Show']
    ]

    with pytest.raises(TypeError):
        format_movie_list(raw_data)


@pytest.fixture
def movie_objects():
    """List of Movie objects for testing."""
    return format_movie_list(MOVIE_DATA)


def test_top_3_movies_correct_selection(movie_objects):
    """Tests if top 3 highest and certified fresh movies are returned."""
    top_movies = get_top_movies(movie_objects, top_n=3)

    # expected ratings should be 9.9, 9.5, 9.1
    assert len(top_movies) == 3
    assert top_movies[0].movie_title == 'Signs'
    assert top_movies[1].movie_title == 'Hereditary'
    assert top_movies[2].movie_title == 'The Conjuring'


def test_top_n_larger_than_data(movie_objects):
    """Tests if top_n is greater than length of certified fresh movies."""
    # there are only 7 certified fresh movies in the test data
    top_movies = get_top_movies(movie_objects, top_n=100)
    assert len(top_movies) == 7
    # list should still be sorted
    assert top_movies[0].rating == 9.9
    assert top_movies[-1].rating == 7.0


def test_empty_input():
    """Tests where the list is empty."""
    assert get_top_movies([], top_n=5) == []


def test_no_certified_fresh():
    """Tests where no movies are certified fresh."""
    bad_data = [Movie(id, 5.0, f"Bad {id}", False) for id in range(5)]
    assert get_top_movies(bad_data, top_n=5) == []


def test_top_not_fresh(movie_objects):
    """Tests where the criteria is no certified fresh."""
    top_not_fresh = get_top_movies(
        movie_objects,
        top_n=5,
        condition_checker=lambda mov: not mov.certified_fresh
    )
    assert len(top_not_fresh) == 2
    assert top_not_fresh[0].movie_title == '28 Days Later'
    assert top_not_fresh[1].movie_title == 'Evil Dead Rise'
