from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(routes["register"], view_func=routes["register_controllers"])
app.add_url_rule(routes["login"], view_func=routes["login_controllers"])
app.add_url_rule(routes["products"], view_func=routes["products_controllers"])
app.add_url_rule(routes["orders"], view_func=routes["orders_controllers"])
app.add_url_rule(routes["fav"], view_func=routes["fav_controllers"])


