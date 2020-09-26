import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = 'postgresql://postgres:rafay@localhost:5432/api_database'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movie_db.movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URI)

