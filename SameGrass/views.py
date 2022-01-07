from flask import Blueprint, render_template, request

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")




# @views.route("/getdata")
# def getdata():
#     args = request.args
#     data = args.get('data')
#     return render_template("index.html", data=name)
