from flask import Flask
from .main.routers import main
from .extensions import mongo

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb+srv://admin:l3MswVbXsL1XBBus@mymongodb.i5h0p.mongodb.net/mydb?retryWrites=true&w=majority'
    mongo.init_app(app)
    app.register_blueprint(main)
    return app

