from flask import flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app= Flask(__name__)

app.config['SECRET_KEY']= "abc123"

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False 

connect_db(app)
db.create.all()


toolbar = DebugToolbarExtension(app)


@app.route("/")
def list_pets():
    """Lists of Pets"""
    pets = Pet.query.all()
    return render_template("Pet_list.html", pets=pets)

@app.route("/add", methods="["GET", "POST"])
def add_pet():
    """Add new pet"""

    form = AddPetForm()
#check to see if form is valid
    if form.validate_on_submit()
        data = {k: v for k, v in form.data.time() if k !="crsf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added!")
        return redirect(url_for('lists_pets'))
#else we will return back to the original form
    else
        return render_template("pet_add_form.html", form=form)

@app.route("/<int:pet_id", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit Pets"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated")
        return redirect(url_for('lists_pets'))

    else
        return render_template("pet_edit_form.html", form=form, pet=pet)

@ap.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Returns basic info about the Pets in JSON"""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age":pet.age}
    return jsonify(info)

    