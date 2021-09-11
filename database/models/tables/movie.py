from database.db import db


class Movie(db.Model):

    def __init__(self, title, year, description, rating, ranking, review):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        super().__init__()

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    year = db.Column(db.Date)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))

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
