from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template("show_dojos.html", all_dojos=dojos)

@app.route("/add_dojo/", methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["name"]
    }
    dojo = Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_ninjas(data)
    return render_template("show.html", dojo=dojo)