from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    
    from controllers.restraunt_controller import restaurant_bp
    from controllers.pizza_controller import pizza_bp
    from controllers.restraunt_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app
