from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

p1 = Pet(name='Spanky', species='cat', photo_url='https://cdn.pixabay.com/photo/2013/04/01/03/45/cat-98359_1280.jpg',
        age='30', notes='cute', available=True)

p2 = Pet(name='Otto', species='cat', photo_url='https://cdn.pixabay.com/photo/2017/03/29/09/59/cat-2184682_1280.jpg',
        age='30', available=True)

db.session.add_all([p1,p2])
db.session.commit()