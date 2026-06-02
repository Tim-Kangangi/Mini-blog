from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)
    CORS(app)

    app.register_blueprint(bp)

    @app.route("/")
    def home():
        return {"msg": "running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)