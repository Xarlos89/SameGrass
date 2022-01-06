from flask import Blueprint, render_template, request
from Functions import *

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html", name="Xarlos")


# @views.route("/getdata")
# def getdata():
#     args = request.args
#     data = args.get('data')
#     return render_template("index.html", data=name)
