from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petclinic.db'  # Replace with your database URI
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Ensure the database tables are created when the app starts
    with app.app_context():
        db.create_all()

    # Import and register the Blueprint here
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    if __name__ == '__main__':
        app.run(debug=True)
    
    return app
