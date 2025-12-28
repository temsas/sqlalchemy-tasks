from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def format_movie(movie):
    return (
        f"{movie.title} by {movie.director}, released on {movie.release_date}, "
        f"duration: {movie.duration} min, genre: {movie.genre}, rating: {movie.rating}"
    )

def get_all_movies(session):
    query = select(Movie)
    movies = session.execute(query).scalars().all()
    return [format_movie(movie) for movie in movies]

def get_movies_by_director(session, director_name):
    query = select(Movie).where(Movie.director == director_name).order_by(Movie.release_date)
    movies = session.execute(query).scalars().all()
    return [format_movie(movie) for movie in movies]

def get_top_rated_movies(session, n):
    query = select(Movie).order_by(Movie.rating.desc())
    movies = session.execute(query).scalars().all()[:n]
    return [format_movie(movie) for movie in movies]
# END
