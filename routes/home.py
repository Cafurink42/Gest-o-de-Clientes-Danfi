from flask import Blueprint, render_template




#blueprint agrupa rotas

home_route = Blueprint("home", __name__)

@home_route.route("/")

def home():
    return render_template("index.html")