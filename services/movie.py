from typing import Optional, List
from django.db.models import QuerySet
from db.models import Movie


def get_movies(
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Optional[QuerySet]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    elif genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)

    return None


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
