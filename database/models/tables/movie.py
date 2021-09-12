from database.db import db
from dataclasses import dataclass


@dataclass
class Movie(db.Model):

    id: int
    title: str
    description: str
    rating: int
    ranking: int
    review: str

    def __init__(self, title, description, rating, ranking, review):
        self.title = title
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.rating} - {self.description}'

    @classmethod
    def get_all_movies(cls):
        return cls.query.all()

    @classmethod
    def create(cls, **kwargs):
        movie = cls(**kwargs)
        return movie.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete_movie(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_movie(cls, id):
        return cls.query.get(id)

    