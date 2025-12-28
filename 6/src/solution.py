from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
from sqlalchemy import select
def get_movies_with_directors(session):
    query = select(Movie).options(joinedload(Movie.director)).order_by(Movie.title)
    return session.execute(query).scalars().all()
# END
