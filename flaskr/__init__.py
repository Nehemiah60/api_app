from flask import Flask,jsonify
from flask_cors import CORS 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MyKeyisPerfecooo'
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:nehecode@localhost:5432/plantsdb'
    CORS(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods','GET, POST, PATCH, DELETE, OPTIONS')
        return response


    from flaskr.views import bp
    import flaskr.models
    app.register_blueprint(bp)
    return app