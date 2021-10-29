from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template("ninja.html", all_ninjas=ninjas, all_dojos=dojos)

@app.route("/create_ninja", methods=["POST"])
def render_lists():
    data = {
        "dojo_id" : request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    ninja = Ninja.save(data)
    return redirect("/dojos")