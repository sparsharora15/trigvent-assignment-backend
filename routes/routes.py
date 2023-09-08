from flask import Blueprint
from controllers.controllers import create_text,get_text,add_menu_items,get_menu,get_us_population_data

data_routes = Blueprint('textRoutes', __name__)
data_routes.route("/api/texts", methods=["POST"])(create_text)
data_routes.route("/api/add_menu_items", methods=["POST"])(add_menu_items)
data_routes.route("/api/rules/about", methods=["GET"])(get_text)
data_routes.route("/api/getMenu", methods=["GET"])(get_menu)
data_routes.route("/api/rules/us_population", methods=["GET"])(get_us_population_data)