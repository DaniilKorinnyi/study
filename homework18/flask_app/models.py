from flask_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'User #{self.id}'

    def __iter__(self):
        return iter([self.id, self.name, self.age])

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __iter__(self):
        return iter([self.id, self.title, self.author, self.price])


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def __iter__(self):
        return iter([self.id, self.user_id, self.book_id, self.total_price])