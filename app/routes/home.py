from flask import Flask,Blueprint ,render_template, request, redirect, url_for

home_route = Blueprint('home', __name__, template_folder='../templates')

@home_route.route('/')
def inicial():
    return render_template("home.html")