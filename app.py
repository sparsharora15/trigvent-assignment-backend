from flask import Flask
from routes.routes import data_routes
from config import Config
from flask_migrate import Migrate
from models.db import db
from flask_cors import CORS

def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    Migrate(app, db)
    db.init_app(app)
    app.register_blueprint(data_routes, url_prefix="/")

    return app

app = createApp()
CORS(app, support_credentials=True)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
