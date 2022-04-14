from flask_sqlalchemy import SQLAchemy

GENERIC_IMAGE = "https://www.publicdomainpictures.net/pictures/150000/nahled/pet-silhouette-icons.jpg"

db = SQLAchemy()

class Pet(db.model):
    """Adoptable Pets"""

    __tablename__ = "Pets"

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url()
    """Returns the image of pet"""

        return self.photo.url or GENERIC_IMAGE

def connect_db(app):
    """connect db to flask app"""

    db.app = app
    db.init_app(app)
    