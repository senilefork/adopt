from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets_table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def example_data():
    Pet.query.delete()

    p1 = Pet(name='Spanky', species='cat', photo_url='https://cdn.pixabay.com/photo/2013/04/01/03/45/cat-98359_1280.jpg',
            age='30', notes='cute', available=True)

    p2 = Pet(name='Otto', species='cat', photo_url='https://cdn.pixabay.com/photo/2017/03/29/09/59/cat-2184682_1280.jpg',
            age='30', available=True)

    db.session.add_all([p1,p2])
    db.session.commit()

def connect_db(app):
    """Connect the database to our Flask app."""

    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from app import app
    connect_db(app)

    db.drop_all()
    db.create_all()
    example_data()





# Create a single model, Pet. This models a pet potentially available for adoption:

# id: auto-incrementing integer
# name: text, required
# species: text, required
# photo_url: text, optional
# age: integer, optional
# notes: text, optional
# available: true/false, required, should default to available