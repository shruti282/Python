from flask import Blueprint, render_template

homepage = Blueprint(__name__, "homepage")

@homepage.route("/")
def home():
    return render_template("index.html", user = "USER")
