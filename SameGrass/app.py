from flask import Flask
from views import views
from Functions import *
from Menu import menu

# Added webhook to server
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)