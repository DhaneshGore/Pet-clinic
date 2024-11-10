from flask import Flask
from app.routes import bp as main_bp


app = Flask(__name__, template_folder="app/templates")

# Register the blueprint
app.register_blueprint(main_bp)
