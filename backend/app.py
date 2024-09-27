from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the app with your database and other settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db and migrations
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import blueprints and register them
    from api.user_profile import user_profile_bp
    app.register_blueprint(user_profile_bp)

    return app
